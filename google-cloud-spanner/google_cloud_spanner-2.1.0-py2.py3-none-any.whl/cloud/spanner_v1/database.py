# Copyright 2016 Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""User friendly container for Cloud Spanner Database."""

import copy
import functools
import grpc
import re
import threading

import google.auth.credentials
from google.api_core.retry import Retry
from google.api_core.retry import if_exception_type
from google.cloud.exceptions import NotFound
from google.api_core.exceptions import Aborted
import six

# pylint: disable=ungrouped-imports
from google.cloud.spanner_admin_database_v1 import Database as DatabasePB
from google.cloud.spanner_v1._helpers import (
    _merge_query_options,
    _metadata_with_prefix,
)
from google.cloud.spanner_v1.batch import Batch
from google.cloud.spanner_v1.keyset import KeySet
from google.cloud.spanner_v1.pool import BurstyPool
from google.cloud.spanner_v1.pool import SessionCheckout
from google.cloud.spanner_v1.session import Session
from google.cloud.spanner_v1.snapshot import _restart_on_unavailable
from google.cloud.spanner_v1.snapshot import Snapshot
from google.cloud.spanner_v1.streamed import StreamedResultSet
from google.cloud.spanner_v1 import SpannerClient
from google.cloud.spanner_v1.services.spanner.transports.grpc import (
    SpannerGrpcTransport,
)
from google.cloud.spanner_admin_database_v1 import CreateDatabaseRequest
from google.cloud.spanner_admin_database_v1 import UpdateDatabaseDdlRequest
from google.cloud.spanner_v1 import ExecuteSqlRequest
from google.cloud.spanner_v1 import (
    TransactionSelector,
    TransactionOptions,
)

# pylint: enable=ungrouped-imports


SPANNER_DATA_SCOPE = "https://www.googleapis.com/auth/spanner.data"


_DATABASE_NAME_RE = re.compile(
    r"^projects/(?P<project>[^/]+)/"
    r"instances/(?P<instance_id>[a-z][-a-z0-9]*)/"
    r"databases/(?P<database_id>[a-z][a-z0-9_\-]*[a-z0-9])$"
)

_DATABASE_METADATA_FILTER = "name:{0}/operations/"

DEFAULT_RETRY_BACKOFF = Retry(initial=0.02, maximum=32, multiplier=1.3)


class Database(object):
    """Representation of a Cloud Spanner Database.

    We can use a :class:`Database` to:

    * :meth:`create` the database
    * :meth:`reload` the database
    * :meth:`update` the database
    * :meth:`drop` the database

    :type database_id: str
    :param database_id: The ID of the database.

    :type instance: :class:`~google.cloud.spanner_v1.instance.Instance`
    :param instance: The instance that owns the database.

    :type ddl_statements: list of string
    :param ddl_statements: (Optional) DDL statements, excluding the
                           CREATE DATABASE statement.

    :type pool: concrete subclass of
                :class:`~google.cloud.spanner_v1.pool.AbstractSessionPool`.
    :param pool: (Optional) session pool to be used by database.  If not
                 passed, the database will construct an instance of
                 :class:`~google.cloud.spanner_v1.pool.BurstyPool`.
    """

    _spanner_api = None

    def __init__(self, database_id, instance, ddl_statements=(), pool=None):
        self.database_id = database_id
        self._instance = instance
        self._ddl_statements = _check_ddl_statements(ddl_statements)
        self._local = threading.local()
        self._state = None
        self._create_time = None
        self._restore_info = None

        if pool is None:
            pool = BurstyPool()

        self._pool = pool
        pool.bind(self)

    @classmethod
    def from_pb(cls, database_pb, instance, pool=None):
        """Creates an instance of this class from a protobuf.

        :type database_pb:
            :class:`~google.cloud.spanner_admin_instance_v1.Instance`
        :param database_pb: A instance protobuf object.

        :type instance: :class:`~google.cloud.spanner_v1.instance.Instance`
        :param instance: The instance that owns the database.

        :type pool: concrete subclass of
                    :class:`~google.cloud.spanner_v1.pool.AbstractSessionPool`.
        :param pool: (Optional) session pool to be used by database.

        :rtype: :class:`Database`
        :returns: The database parsed from the protobuf response.
        :raises ValueError:
            if the instance name does not match the expected format
            or if the parsed project ID does not match the project ID
            on the instance's client, or if the parsed instance ID does
            not match the instance's ID.
        """
        match = _DATABASE_NAME_RE.match(database_pb.name)
        if match is None:
            raise ValueError(
                "Database protobuf name was not in the " "expected format.",
                database_pb.name,
            )
        if match.group("project") != instance._client.project:
            raise ValueError(
                "Project ID on database does not match the "
                "project ID on the instance's client"
            )
        instance_id = match.group("instance_id")
        if instance_id != instance.instance_id:
            raise ValueError(
                "Instance ID on database does not match the "
                "Instance ID on the instance"
            )
        database_id = match.group("database_id")

        return cls(database_id, instance, pool=pool)

    @property
    def name(self):
        """Database name used in requests.

        .. note::

          This property will not change if ``database_id`` does not, but the
          return value is not cached.

        The database name is of the form

            ``"projects/../instances/../databases/{database_id}"``

        :rtype: str
        :returns: The database name.
        """
        return self._instance.name + "/databases/" + self.database_id

    @property
    def state(self):
        """State of this database.

        :rtype: :class:`~google.cloud.spanner_admin_database_v1.Database.State`
        :returns: an enum describing the state of the database
        """
        return self._state

    @property
    def create_time(self):
        """Create time of this database.

        :rtype: :class:`datetime.datetime`
        :returns: a datetime object representing the create time of
            this database
        """
        return self._create_time

    @property
    def restore_info(self):
        """Restore info for this database.

        :rtype: :class:`~google.cloud.spanner_v1.database.RestoreInfo`
        :returns: an object representing the restore info for this database
        """
        return self._restore_info

    @property
    def ddl_statements(self):
        """DDL Statements used to define database schema.

        See
        cloud.google.com/spanner/docs/data-definition-language

        :rtype: sequence of string
        :returns: the statements
        """
        return self._ddl_statements

    @property
    def spanner_api(self):
        """Helper for session-related API calls."""
        if self._spanner_api is None:
            client_info = self._instance._client._client_info
            client_options = self._instance._client._client_options
            if self._instance.emulator_host is not None:
                transport = SpannerGrpcTransport(
                    channel=grpc.insecure_channel(self._instance.emulator_host)
                )
                self._spanner_api = SpannerClient(
                    client_info=client_info, transport=transport
                )
                return self._spanner_api
            credentials = self._instance._client.credentials
            if isinstance(credentials, google.auth.credentials.Scoped):
                credentials = credentials.with_scopes((SPANNER_DATA_SCOPE,))
            self._spanner_api = SpannerClient(
                credentials=credentials,
                client_info=client_info,
                client_options=client_options,
            )
        return self._spanner_api

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
            other.database_id == self.database_id and other._instance == self._instance
        )

    def __ne__(self, other):
        return not self == other

    def create(self):
        """Create this database within its instance

        Inclues any configured schema assigned to :attr:`ddl_statements`.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateDatabase

        :rtype: :class:`~google.api_core.operation.Operation`
        :returns: a future used to poll the status of the create request
        :raises Conflict: if the database already exists
        :raises NotFound: if the instance owning the database does not exist
        """
        api = self._instance._client.database_admin_api
        metadata = _metadata_with_prefix(self.name)
        db_name = self.database_id
        if "-" in db_name:
            db_name = "`%s`" % (db_name,)

        request = CreateDatabaseRequest(
            parent=self._instance.name,
            create_statement="CREATE DATABASE %s" % (db_name,),
            extra_statements=list(self._ddl_statements),
        )
        future = api.create_database(request=request, metadata=metadata)
        return future

    def exists(self):
        """Test whether this database exists.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDDL

        :rtype: bool
        :returns: True if the database exists, else false.
        """
        api = self._instance._client.database_admin_api
        metadata = _metadata_with_prefix(self.name)

        try:
            api.get_database_ddl(database=self.name, metadata=metadata)
        except NotFound:
            return False
        return True

    def reload(self):
        """Reload this database.

        Refresh any configured schema into :attr:`ddl_statements`.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDDL

        :raises NotFound: if the database does not exist
        """
        api = self._instance._client.database_admin_api
        metadata = _metadata_with_prefix(self.name)
        response = api.get_database_ddl(database=self.name, metadata=metadata)
        self._ddl_statements = tuple(response.statements)
        response = api.get_database(name=self.name, metadata=metadata)
        self._state = DatabasePB.State(response.state)
        self._create_time = response.create_time
        self._restore_info = response.restore_info

    def update_ddl(self, ddl_statements, operation_id=""):
        """Update DDL for this database.

        Apply any configured schema from :attr:`ddl_statements`.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase

        :type ddl_statements: Sequence[str]
        :param ddl_statements: a list of DDL statements to use on this database
        :type operation_id: str
        :param operation_id: (optional) a string ID for the long-running operation

        :rtype: :class:`google.api_core.operation.Operation`
        :returns: an operation instance
        :raises NotFound: if the database does not exist
        """
        client = self._instance._client
        api = client.database_admin_api
        metadata = _metadata_with_prefix(self.name)

        request = UpdateDatabaseDdlRequest(
            database=self.name, statements=ddl_statements, operation_id=operation_id,
        )

        future = api.update_database_ddl(request=request, metadata=metadata)
        return future

    def drop(self):
        """Drop this database.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.DropDatabase
        """
        api = self._instance._client.database_admin_api
        metadata = _metadata_with_prefix(self.name)
        api.drop_database(database=self.name, metadata=metadata)

    def execute_partitioned_dml(
        self, dml, params=None, param_types=None, query_options=None
    ):
        """Execute a partitionable DML statement.

        :type dml: str
        :param dml: DML statement

        :type params: dict, {str -> column value}
        :param params: values for parameter replacement.  Keys must match
                       the names used in ``dml``.

        :type param_types: dict[str -> Union[dict, .types.Type]]
        :param param_types:
            (Optional) maps explicit types for one or more param values;
            required if parameters are passed.

        :type query_options:
            :class:`~google.cloud.spanner_v1.ExecuteSqlRequest.QueryOptions`
            or :class:`dict`
        :param query_options:
                (Optional) Query optimizer configuration to use for the given query.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.spanner_v1.QueryOptions`

        :rtype: int
        :returns: Count of rows affected by the DML statement.
        """
        query_options = _merge_query_options(
            self._instance._client._query_options, query_options
        )
        if params is not None:
            from google.cloud.spanner_v1.transaction import Transaction

            if param_types is None:
                raise ValueError("Specify 'param_types' when passing 'params'.")
            params_pb = Transaction._make_params_pb(params, param_types)
        else:
            params_pb = {}

        api = self.spanner_api

        txn_options = TransactionOptions(
            partitioned_dml=TransactionOptions.PartitionedDml()
        )

        metadata = _metadata_with_prefix(self.name)

        def execute_pdml():
            with SessionCheckout(self._pool) as session:

                txn = api.begin_transaction(
                    session=session.name, options=txn_options, metadata=metadata
                )

                txn_selector = TransactionSelector(id=txn.id)

                request = ExecuteSqlRequest(
                    session=session.name,
                    sql=dml,
                    transaction=txn_selector,
                    params=params_pb,
                    param_types=param_types,
                    query_options=query_options,
                )
                restart = functools.partial(
                    api.execute_streaming_sql, request=request, metadata=metadata,
                )

                iterator = _restart_on_unavailable(restart)

                result_set = StreamedResultSet(iterator)
                list(result_set)  # consume all partials

                return result_set.stats.row_count_lower_bound

        return _retry_on_aborted(execute_pdml, DEFAULT_RETRY_BACKOFF)()

    def session(self, labels=None):
        """Factory to create a session for this database.

        :type labels: dict (str -> str) or None
        :param labels: (Optional) user-assigned labels for the session.

        :rtype: :class:`~google.cloud.spanner_v1.session.Session`
        :returns: a session bound to this database.
        """
        return Session(self, labels=labels)

    def snapshot(self, **kw):
        """Return an object which wraps a snapshot.

        The wrapper *must* be used as a context manager, with the snapshot
        as the value returned by the wrapper.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.v1#google.spanner.v1.TransactionOptions.ReadOnly

        :type kw: dict
        :param kw:
            Passed through to
            :class:`~google.cloud.spanner_v1.snapshot.Snapshot` constructor.

        :rtype: :class:`~google.cloud.spanner_v1.database.SnapshotCheckout`
        :returns: new wrapper
        """
        return SnapshotCheckout(self, **kw)

    def batch(self):
        """Return an object which wraps a batch.

        The wrapper *must* be used as a context manager, with the batch
        as the value returned by the wrapper.

        :rtype: :class:`~google.cloud.spanner_v1.database.BatchCheckout`
        :returns: new wrapper
        """
        return BatchCheckout(self)

    def batch_snapshot(self, read_timestamp=None, exact_staleness=None):
        """Return an object which wraps a batch read / query.

        :type read_timestamp: :class:`datetime.datetime`
        :param read_timestamp: Execute all reads at the given timestamp.

        :type exact_staleness: :class:`datetime.timedelta`
        :param exact_staleness: Execute all reads at a timestamp that is
                                ``exact_staleness`` old.

        :rtype: :class:`~google.cloud.spanner_v1.database.BatchSnapshot`
        :returns: new wrapper
        """
        return BatchSnapshot(
            self, read_timestamp=read_timestamp, exact_staleness=exact_staleness
        )

    def run_in_transaction(self, func, *args, **kw):
        """Perform a unit of work in a transaction, retrying on abort.

        :type func: callable
        :param func: takes a required positional argument, the transaction,
                     and additional positional / keyword arguments as supplied
                     by the caller.

        :type args: tuple
        :param args: additional positional arguments to be passed to ``func``.

        :type kw: dict
        :param kw: (Optional) keyword arguments to be passed to ``func``.
                   If passed, "timeout_secs" will be removed and used to
                   override the default retry timeout which defines maximum timestamp
                   to continue retrying the transaction.

        :rtype: Any
        :returns: The return value of ``func``.

        :raises Exception:
            reraises any non-ABORT execptions raised by ``func``.
        """
        # Sanity check: Is there a transaction already running?
        # If there is, then raise a red flag. Otherwise, mark that this one
        # is running.
        if getattr(self._local, "transaction_running", False):
            raise RuntimeError("Spanner does not support nested transactions.")
        self._local.transaction_running = True

        # Check out a session and run the function in a transaction; once
        # done, flip the sanity check bit back.
        try:
            with SessionCheckout(self._pool) as session:
                return session.run_in_transaction(func, *args, **kw)
        finally:
            self._local.transaction_running = False

    def restore(self, source):
        """Restore from a backup to this database.

        :type backup: :class:`~google.cloud.spanner_v1.backup.Backup`
        :param backup: the path of the backup being restored from.

        :rtype: :class:`~google.api_core.operation.Operation`
        :returns: a future used to poll the status of the create request
        :raises Conflict: if the database already exists
        :raises NotFound:
            if the instance owning the database does not exist, or
            if the backup being restored from does not exist
        :raises ValueError: if backup is not set
        """
        if source is None:
            raise ValueError("Restore source not specified")
        api = self._instance._client.database_admin_api
        metadata = _metadata_with_prefix(self.name)
        future = api.restore_database(
            parent=self._instance.name,
            database_id=self.database_id,
            backup=source.name,
            metadata=metadata,
        )
        return future

    def is_ready(self):
        """Test whether this database is ready for use.

        :rtype: bool
        :returns: True if the database state is READY_OPTIMIZING or READY, else False.
        """
        return (
            self.state == DatabasePB.State.READY_OPTIMIZING
            or self.state == DatabasePB.State.READY
        )

    def is_optimized(self):
        """Test whether this database has finished optimizing.

        :rtype: bool
        :returns: True if the database state is READY, else False.
        """
        return self.state == DatabasePB.State.READY

    def list_database_operations(self, filter_="", page_size=None):
        """List database operations for the database.

        :type filter_: str
        :param filter_:
            Optional. A string specifying a filter for which database operations to list.

        :type page_size: int
        :param page_size:
            Optional. The maximum number of operations in each page of results from this
            request. Non-positive values are ignored. Defaults to a sensible value set
            by the API.

        :type: :class:`~google.api_core.page_iterator.Iterator`
        :returns:
            Iterator of :class:`~google.api_core.operation.Operation`
            resources within the current instance.
        """
        database_filter = _DATABASE_METADATA_FILTER.format(self.name)
        if filter_:
            database_filter = "({0}) AND ({1})".format(filter_, database_filter)
        return self._instance.list_database_operations(
            filter_=database_filter, page_size=page_size
        )


class BatchCheckout(object):
    """Context manager for using a batch from a database.

    Inside the context manager, checks out a session from the database,
    creates a batch from it, making the batch available.

    Caller must *not* use the batch to perform API requests outside the scope
    of the context manager.

    :type database: :class:`~google.cloud.spanner_v1.database.Database`
    :param database: database to use
    """

    def __init__(self, database):
        self._database = database
        self._session = self._batch = None

    def __enter__(self):
        """Begin ``with`` block."""
        session = self._session = self._database._pool.get()
        batch = self._batch = Batch(session)
        return batch

    def __exit__(self, exc_type, exc_val, exc_tb):
        """End ``with`` block."""
        try:
            if exc_type is None:
                self._batch.commit()
        finally:
            self._database._pool.put(self._session)


class SnapshotCheckout(object):
    """Context manager for using a snapshot from a database.

    Inside the context manager, checks out a session from the database,
    creates a snapshot from it, making the snapshot available.

    Caller must *not* use the snapshot to perform API requests outside the
    scope of the context manager.

    :type database: :class:`~google.cloud.spanner_v1.database.Database`
    :param database: database to use

    :type kw: dict
    :param kw:
        Passed through to
        :class:`~google.cloud.spanner_v1.snapshot.Snapshot` constructor.
    """

    def __init__(self, database, **kw):
        self._database = database
        self._session = None
        self._kw = kw

    def __enter__(self):
        """Begin ``with`` block."""
        session = self._session = self._database._pool.get()
        return Snapshot(session, **self._kw)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """End ``with`` block."""
        self._database._pool.put(self._session)


class BatchSnapshot(object):
    """Wrapper for generating and processing read / query batches.

    :type database: :class:`~google.cloud.spanner_v1.database.Database`
    :param database: database to use

    :type read_timestamp: :class:`datetime.datetime`
    :param read_timestamp: Execute all reads at the given timestamp.

    :type exact_staleness: :class:`datetime.timedelta`
    :param exact_staleness: Execute all reads at a timestamp that is
                            ``exact_staleness`` old.
    """

    def __init__(self, database, read_timestamp=None, exact_staleness=None):
        self._database = database
        self._session = None
        self._snapshot = None
        self._read_timestamp = read_timestamp
        self._exact_staleness = exact_staleness

    @classmethod
    def from_dict(cls, database, mapping):
        """Reconstruct an instance from a mapping.

        :type database: :class:`~google.cloud.spanner_v1.database.Database`
        :param database: database to use

        :type mapping: mapping
        :param mapping: serialized state of the instance

        :rtype: :class:`BatchSnapshot`
        """
        instance = cls(database)
        session = instance._session = database.session()
        session._session_id = mapping["session_id"]
        snapshot = instance._snapshot = session.snapshot()
        snapshot._transaction_id = mapping["transaction_id"]
        return instance

    def to_dict(self):
        """Return state as a dictionary.

        Result can be used to serialize the instance and reconstitute
        it later using :meth:`from_dict`.

        :rtype: dict
        """
        session = self._get_session()
        snapshot = self._get_snapshot()
        return {
            "session_id": session._session_id,
            "transaction_id": snapshot._transaction_id,
        }

    def _get_session(self):
        """Create session as needed.

        .. note::

           Caller is responsible for cleaning up the session after
           all partitions have been processed.
        """
        if self._session is None:
            session = self._session = self._database.session()
            session.create()
        return self._session

    def _get_snapshot(self):
        """Create snapshot if needed."""
        if self._snapshot is None:
            self._snapshot = self._get_session().snapshot(
                read_timestamp=self._read_timestamp,
                exact_staleness=self._exact_staleness,
                multi_use=True,
            )
            self._snapshot.begin()
        return self._snapshot

    def read(self, *args, **kw):
        """Convenience method:  perform read operation via snapshot.

        See :meth:`~google.cloud.spanner_v1.snapshot.Snapshot.read`.
        """
        return self._get_snapshot().read(*args, **kw)

    def execute_sql(self, *args, **kw):
        """Convenience method:  perform query operation via snapshot.

        See :meth:`~google.cloud.spanner_v1.snapshot.Snapshot.execute_sql`.
        """
        return self._get_snapshot().execute_sql(*args, **kw)

    def generate_read_batches(
        self,
        table,
        columns,
        keyset,
        index="",
        partition_size_bytes=None,
        max_partitions=None,
    ):
        """Start a partitioned batch read operation.

        Uses the ``PartitionRead`` API request to initiate the partitioned
        read.  Returns a list of batch information needed to perform the
        actual reads.

        :type table: str
        :param table: name of the table from which to fetch data

        :type columns: list of str
        :param columns: names of columns to be retrieved

        :type keyset: :class:`~google.cloud.spanner_v1.keyset.KeySet`
        :param keyset: keys / ranges identifying rows to be retrieved

        :type index: str
        :param index: (Optional) name of index to use, rather than the
                      table's primary key

        :type partition_size_bytes: int
        :param partition_size_bytes:
            (Optional) desired size for each partition generated.  The service
            uses this as a hint, the actual partition size may differ.

        :type max_partitions: int
        :param max_partitions:
            (Optional) desired maximum number of partitions generated. The
            service uses this as a hint, the actual number of partitions may
            differ.

        :rtype: iterable of dict
        :returns:
            mappings of information used peform actual partitioned reads via
            :meth:`process_read_batch`.
        """
        partitions = self._get_snapshot().partition_read(
            table=table,
            columns=columns,
            keyset=keyset,
            index=index,
            partition_size_bytes=partition_size_bytes,
            max_partitions=max_partitions,
        )

        read_info = {
            "table": table,
            "columns": columns,
            "keyset": keyset._to_dict(),
            "index": index,
        }
        for partition in partitions:
            yield {"partition": partition, "read": read_info.copy()}

    def process_read_batch(self, batch):
        """Process a single, partitioned read.

        :type batch: mapping
        :param batch:
            one of the mappings returned from an earlier call to
            :meth:`generate_read_batches`.

        :rtype: :class:`~google.cloud.spanner_v1.streamed.StreamedResultSet`
        :returns: a result set instance which can be used to consume rows.
        """
        kwargs = copy.deepcopy(batch["read"])
        keyset_dict = kwargs.pop("keyset")
        kwargs["keyset"] = KeySet._from_dict(keyset_dict)
        return self._get_snapshot().read(partition=batch["partition"], **kwargs)

    def generate_query_batches(
        self,
        sql,
        params=None,
        param_types=None,
        partition_size_bytes=None,
        max_partitions=None,
        query_options=None,
    ):
        """Start a partitioned query operation.

        Uses the ``PartitionQuery`` API request to start a partitioned
        query operation.  Returns a list of batch information needed to
        peform the actual queries.

        :type sql: str
        :param sql: SQL query statement

        :type params: dict, {str -> column value}
        :param params: values for parameter replacement.  Keys must match
                       the names used in ``sql``.

        :type param_types: dict[str -> Union[dict, .types.Type]]
        :param param_types:
            (Optional) maps explicit types for one or more param values;
            required if parameters are passed.

        :type partition_size_bytes: int
        :param partition_size_bytes:
            (Optional) desired size for each partition generated.  The service
            uses this as a hint, the actual partition size may differ.

        :type partition_size_bytes: int
        :param partition_size_bytes:
            (Optional) desired size for each partition generated.  The service
            uses this as a hint, the actual partition size may differ.

        :type max_partitions: int
        :param max_partitions:
            (Optional) desired maximum number of partitions generated. The
            service uses this as a hint, the actual number of partitions may
            differ.

        :type query_options:
            :class:`~google.cloud.spanner_v1.ExecuteSqlRequest.QueryOptions`
            or :class:`dict`
        :param query_options:
                (Optional) Query optimizer configuration to use for the given query.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.spanner_v1.QueryOptions`

        :rtype: iterable of dict
        :returns:
            mappings of information used peform actual partitioned reads via
            :meth:`process_read_batch`.
        """
        partitions = self._get_snapshot().partition_query(
            sql=sql,
            params=params,
            param_types=param_types,
            partition_size_bytes=partition_size_bytes,
            max_partitions=max_partitions,
        )

        query_info = {"sql": sql}
        if params:
            query_info["params"] = params
            query_info["param_types"] = param_types

        # Query-level options have higher precedence than client-level and
        # environment-level options
        default_query_options = self._database._instance._client._query_options
        query_info["query_options"] = _merge_query_options(
            default_query_options, query_options
        )

        for partition in partitions:
            yield {"partition": partition, "query": query_info}

    def process_query_batch(self, batch):
        """Process a single, partitioned query.

        :type batch: mapping
        :param batch:
            one of the mappings returned from an earlier call to
            :meth:`generate_query_batches`.

        :rtype: :class:`~google.cloud.spanner_v1.streamed.StreamedResultSet`
        :returns: a result set instance which can be used to consume rows.
        """
        return self._get_snapshot().execute_sql(
            partition=batch["partition"], **batch["query"]
        )

    def process(self, batch):
        """Process a single, partitioned query or read.

        :type batch: mapping
        :param batch:
            one of the mappings returned from an earlier call to
            :meth:`generate_query_batches`.

        :rtype: :class:`~google.cloud.spanner_v1.streamed.StreamedResultSet`
        :returns: a result set instance which can be used to consume rows.
        :raises ValueError: if batch does not contain either 'read' or 'query'
        """
        if "query" in batch:
            return self.process_query_batch(batch)
        if "read" in batch:
            return self.process_read_batch(batch)
        raise ValueError("Invalid batch")

    def close(self):
        """Clean up underlying session.

        .. note::

           If the transaction has been shared across multiple machines,
           calling this on any machine would invalidate the transaction
           everywhere. Ideally this would be called when data has been read
           from all the partitions.
        """
        if self._session is not None:
            self._session.delete()


def _check_ddl_statements(value):
    """Validate DDL Statements used to define database schema.

    See
    https://cloud.google.com/spanner/docs/data-definition-language

    :type value: list of string
    :param value: DDL statements, excluding the 'CREATE DATABSE' statement

    :rtype: tuple
    :returns: tuple of validated DDL statement strings.
    :raises ValueError:
        if elements in ``value`` are not strings, or if ``value`` contains
        a ``CREATE DATABASE`` statement.
    """
    if not all(isinstance(line, six.string_types) for line in value):
        raise ValueError("Pass a list of strings")

    if any("create database" in line.lower() for line in value):
        raise ValueError("Do not pass a 'CREATE DATABASE' statement")

    return tuple(value)


def _retry_on_aborted(func, retry_config):
    """Helper for :meth:`Database.execute_partitioned_dml`.

    Wrap function in a Retry that will retry on Aborted exceptions
    with the retry config specified.

    :type func: callable
    :param func: the function to be retried on Aborted exceptions

    :type retry_config: Retry
    :param retry_config: retry object with the settings to be used
    """
    retry = retry_config.with_predicate(if_exception_type(Aborted))
    return retry(func)
