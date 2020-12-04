"""
Setup an health_check API.

To use it, create an instance of this class in your application initialization and do a few calls to its
methods add_db_check()
"""
import configparser
import copy
import logging
import os
import re
import subprocess
import time
import traceback
from collections import Counter
from enum import Enum
from typing import Any, Callable, Dict, List, Mapping, Optional, Tuple, Union

import pyramid.config
import pyramid.request
import requests
import sqlalchemy.engine
import sqlalchemy.orm
from pyramid.httpexceptions import HTTPNotFound

from c2cwsgiutils import _utils, auth, broadcast, redis_utils, stats, version

LOG = logging.getLogger(__name__)
ALEMBIC_HEAD_RE = re.compile(r"^([a-f0-9]+) \(head\)\n$")


class EngineType(Enum):
    READ_ONLY = 1
    WRITE_ONLY = 2
    READ_AND_WRITE = 3


class JsonCheckException(Exception):
    """
    Checker exception used to add some structured content to a failure.
    """

    def __init__(self, message: str, json: Any):
        super().__init__()
        self.message = message
        self.json = json

    def __str__(self) -> str:
        return self.message

    def json_data(self) -> Any:
        return self.json


def _get_bindings(session: Any, engine_type: EngineType) -> List[sqlalchemy.engine.Engine]:
    if session.c2c_rw_bind == session.c2c_ro_bind:
        engine_type = EngineType.WRITE_ONLY

    if engine_type == EngineType.READ_AND_WRITE:
        return [session.c2c_rw_bind, session.c2c_ro_bind]
    if engine_type == EngineType.READ_ONLY:
        return [session.c2c_ro_bind]
    if engine_type == EngineType.WRITE_ONLY:
        return [session.c2c_rw_bind]
    raise NotImplementedError("Unhandled engine type %s" % engine_type)


def _get_alembic_version(alembic_ini_path: str, name: str) -> str:
    # Go to the directory holding the config file and add '.' to the PYTHONPATH variable to support Alembic
    # migration scripts using common modules
    env = dict(os.environ)
    pythonpath = os.environ.get("PYTHONPATH", "")
    pythonpath = (pythonpath + ":" if pythonpath else "") + "."
    env["PYTHONPATH"] = pythonpath
    dirname = os.path.abspath(os.path.dirname(alembic_ini_path))

    out = subprocess.check_output(
        ["alembic", "--config", alembic_ini_path, "--name", name, "heads"], cwd=dirname, env=env
    ).decode("utf-8")
    out_match = ALEMBIC_HEAD_RE.match(out)
    if not out_match:
        raise Exception("Cannot get the alembic HEAD version from: " + out)
    return out_match.group(1)


class HealthCheck:
    """
    Class for managing health checks.

    Only one instance of this class must be created per process.
    """

    def __init__(self, config: pyramid.config.Configurator) -> None:
        config.add_route(
            "c2c_health_check", _utils.get_base_path(config) + r"/health_check", request_method="GET"
        )
        config.add_view(self._view, route_name="c2c_health_check", renderer="fast_json", http_cache=0)
        self._checks: List[Tuple[str, Callable[[pyramid.request.Request], Any], int]] = []

        redis = os.environ.get(redis_utils.REDIS_SENTINELS_KEY, os.environ.get(redis_utils.REDIS_URL_KEY))
        if redis:
            self.add_redis_check(level=2)
            if version.get_version() is not None:
                self.add_version_check(level=2)

    def add_db_session_check(
        self,
        session: sqlalchemy.orm.scoping.scoped_session,
        query_cb: Optional[Callable[[sqlalchemy.orm.scoping.scoped_session], Any]] = None,
        at_least_one_model: Optional[object] = None,
        level: int = 1,
        engine_type: EngineType = EngineType.READ_AND_WRITE,
    ) -> None:
        """
        Check a DB session is working. You can specify either query_cb or at_least_one_model.

        :param session: a DB session created by c2cwsgiutils.db.setup_session()
        :param query_cb: a callable that take a session as parameter and check it works
        :param at_least_one_model: a model that must have at least one entry in the DB
        :param level: the level of the health check
        :param engine_type: whether to check only the RW, RO or both engines
        """
        if query_cb is None:
            query_cb = self._at_least_one(at_least_one_model)
        for binding in _get_bindings(session, engine_type):
            name, cb = self._create_db_engine_check(session, binding, query_cb)
            assert name
            self._checks.append((name, cb, level))

    def add_alembic_check(
        self,
        session: sqlalchemy.orm.scoping.scoped_session,
        alembic_ini_path: str,
        level: int = 2,
        name: str = "alembic",
        version_schema: Optional[str] = None,
        version_table: Optional[str] = None,
    ) -> None:
        """
        Check the DB version against the HEAD version of Alembic.

        :param session: A DB session created by c2cwsgiutils.db.setup_session() giving access to the DB \
                        managed by Alembic
        :param alembic_ini_path: Path to the Alembic INI file
        :param level: the level of the health check
        :param name: the name of the configuration section in the Alembic INI file
        :param version_schema: override the schema where the version table is
        :param version_table: override the table name for the version
        """
        version_ = _get_alembic_version(alembic_ini_path, name)

        config = configparser.ConfigParser()
        config.read(alembic_ini_path)

        if version_schema is None:
            version_schema = config.get(name, "version_table_schema", fallback="public")

        if version_table is None:
            version_table = config.get(name, "version_table", fallback="alembic_version")

        def check(_request: Any) -> str:
            for binding in _get_bindings(session, EngineType.READ_AND_WRITE):
                prev_bind = session.bind
                try:
                    session.bind = binding
                    if stats.USE_TAGS:
                        key = ["sql", "manual", "health_check", "alembic"]
                        tags: Optional[Dict[str, str]] = dict(conf=alembic_ini_path, con=binding.c2c_name)
                    else:
                        key = ["sql", "manual", "health_check", "alembic", alembic_ini_path, binding.c2c_name]
                        tags = None
                    with stats.timer_context(key, tags):
                        quote = session.bind.dialect.identifier_preparer.quote
                        (actual_version,) = session.execute(
                            "SELECT version_num FROM {schema}.{table}".format(  # nosec
                                schema=quote(version_schema), table=quote(version_table)
                            )
                        ).fetchone()
                        if stats.USE_TAGS:
                            stats.increment_counter(
                                ["alembic_version"], 1, tags=dict(version=actual_version, name=name)
                            )
                        else:
                            stats.increment_counter(["alembic_version", name, actual_version], 1)
                        if actual_version != version_:
                            raise Exception(
                                "Invalid alembic version (db: %s, code: %s)" % (actual_version, version_)
                            )
                finally:
                    session.bind = prev_bind
            return version_

        self._checks.append(
            ("alembic_" + alembic_ini_path.replace("/", "_").strip("_") + "_" + name, check, level)
        )

    def add_url_check(
        self,
        url: Union[str, Callable[[pyramid.request.Request], str]],
        params: Union[Mapping[str, str], Callable[[pyramid.request.Request], Mapping[str, str]], None] = None,
        headers: Union[
            Mapping[str, str], Callable[[pyramid.request.Request], Mapping[str, str]], None
        ] = None,
        name: Optional[str] = None,
        check_cb: Callable[
            [pyramid.request.Request, requests.Response], Any
        ] = lambda request, response: None,
        timeout: float = 3,
        level: int = 1,
    ) -> None:
        """
        Check that a GET on an URL returns 2xx

        :param url: the URL to query or a function taking the request and returning it
        :param params: the parameters or a function taking the request and returning them
        :param headers: the headers or a function taking the request and returning them
        :param name: the name of the check (defaults to url)
        :param check_cb: an optional CB to do additional checks on the response (takes the request and the \
                         response as parameters)
        :param timeout: the timeout
        :param level: the level of the health check
        """

        def check(request: pyramid.request.Request) -> Any:
            the_url = _maybe_function(url, request)
            the_params = _maybe_function(params, request)
            the_headers = copy.deepcopy(_maybe_function(headers, request) if headers is not None else {})
            the_headers.update({"X-Request-ID": request.c2c_request_id})

            response = requests.get(the_url, timeout=timeout, params=the_params, headers=the_headers)
            response.raise_for_status()
            return check_cb(request, response)

        if name is None:
            name = str(url)
        assert name
        self._checks.append((name, check, level))

    def add_redis_check(self, name: Optional[str] = None, level: int = 1) -> None:
        """
        Check that the given redis server is reachable. One such check is automatically added if
        the broadcaster is configured with redis.

        :param name: the name of the check (defaults to url)
        :param level: the level of the health check
        :return:
        """

        def check(request: pyramid.request.Request) -> Any:
            master, slave, sentinel = redis_utils.get()

            result = {}

            def add(name: str, func: Callable[..., Any], *args: Any) -> None:
                try:
                    result[name] = func(*args)
                except Exception as e:  # pylint: disable=broad-except
                    result[name] = {"error": str(e)}

            if master is not None:
                add("info", master.info)
                add("info", master.dbsize)
            if slave is not None:
                add("slave_info", slave.info)
            if sentinel is not None:
                service_name = os.environ.get(redis_utils.REDIS_SERVICENAME_KEY, "mymaster")
                add("sentinel", sentinel.sentinels[0].sentinel)
                add("sentinel_masters", sentinel.sentinels[0].sentinel_masters)
                add("sentinel_master", sentinel.sentinels[0].sentinel_master, service_name)
                add("sentinel_sentinels", sentinel.sentinels[0].sentinel_sentinels, service_name)
                add("sentinel_slaves", sentinel.sentinels[0].sentinel_slaves, service_name)

            return result

        if name is None:
            name = os.environ.get(redis_utils.REDIS_SENTINELS_KEY, os.environ.get(redis_utils.REDIS_URL_KEY))
        assert name
        self._checks.append((name, check, level))

    def add_version_check(self, name: str = "version", level: int = 2) -> None:
        """
        Check that the version matches across all instances
        :param name: the name of the check (defaults to "version")
        :param level: the level of the health check
        :return:
        """

        def check(request: pyramid.request.Request) -> Any:
            versions = _get_all_versions()
            versions = list(filter(lambda x: x is not None, versions))
            assert versions
            # Output the versions we see on the monitoring
            v: Optional[str]
            for v, count in Counter(versions).items():
                if stats.USE_TAGS:
                    stats.increment_counter(["version"], count, tags=dict(version=v))
                else:
                    stats.increment_counter(["version", v], count)

                ref = versions[0]
            assert all(v == ref for v in versions), "Non identical versions: " + ", ".join(versions)
            return dict(version=ref, count=len(versions))

        assert name
        self._checks.append((name, check, level))

    def add_custom_check(
        self, name: str, check_cb: Callable[[pyramid.request.Request], Any], level: int = 1
    ) -> None:
        """
        Add a custom check.

        In case of success the callback can return a result (must be serializable to JSON) that will show up
        in the response. In case of failure it must raise an exception.

        :param name: the name of the check
        :param check_cb: the callback to call (takes the request as parameter)
        :param level: the level of the health check
        """
        assert name
        self._checks.append((name, check_cb, level))

    def _view(self, request: pyramid.request.Request) -> Mapping[str, Any]:
        max_level = int(request.params.get("max_level", "1"))
        is_auth = auth.is_auth(request)
        results: Dict[str, Dict[str, Any]] = {
            "failures": {},
            "successes": {},
        }
        checks = None
        if "checks" in request.params:
            if request.params["checks"] != "":
                checks = request.params["checks"].split(",")
        for name, check, level in self._checks:
            if level <= max_level and (checks is None or name in checks):
                self._run_one(check, is_auth, level, name, request, results)

        if results["failures"]:
            request.response.status = 500

        return results

    @staticmethod
    def _run_one(
        check: Callable[[pyramid.request.Request], Any],
        is_auth: bool,
        level: int,
        name: str,
        request: pyramid.request.Request,
        results: Dict[str, Dict[str, Any]],
    ) -> None:
        start = time.monotonic()
        try:
            result = check(request)
            results["successes"][name] = {"timing": time.monotonic() - start, "level": level}
            if result is not None:
                results["successes"][name]["result"] = result
            if stats.USE_TAGS:
                stats.increment_counter(["health_check"], 1, tags=dict(name=name, outcome="success"))
            else:
                stats.increment_counter(["health_check", name, "success"], 1)
        except Exception as e:  # pylint: disable=broad-except
            if stats.USE_TAGS:
                stats.increment_counter(["health_check"], 1, tags=dict(name=name, outcome="failure"))
            else:
                stats.increment_counter(["health_check", name, "failure"], 1)
            LOG.warning("Health check %s failed", name, exc_info=True)
            failure = {"message": str(e), "timing": time.monotonic() - start, "level": level}
            if isinstance(e, JsonCheckException) and e.json_data() is not None:
                failure["result"] = e.json_data()
            if is_auth or os.environ.get("DEVELOPMENT", "0") != "0":
                failure["stacktrace"] = traceback.format_exc()
            results["failures"][name] = failure

    @staticmethod
    def _create_db_engine_check(
        session: sqlalchemy.orm.scoping.scoped_session,
        bind: sqlalchemy.engine.Engine,
        query_cb: Callable[[sqlalchemy.orm.scoping.scoped_session], None],
    ) -> Tuple[str, Callable[[pyramid.request.Request], None]]:
        def check(_request: pyramid.request.Request) -> None:
            prev_bind = session.bind
            try:
                session.bind = bind
                if stats.USE_TAGS:
                    key = ["sql", "manual", "health_check", "db"]
                    tags: Optional[Dict[str, str]] = dict(con=bind.c2c_name)
                else:
                    key = ["sql", "manual", "health_check", "db", bind.c2c_name]
                    tags = None
                with stats.timer_context(key, tags):
                    return query_cb(session)
            finally:
                session.bind = prev_bind

        return "db_engine_" + bind.c2c_name, check

    @staticmethod
    def _at_least_one(model: Any) -> Callable[[sqlalchemy.orm.scoping.scoped_session], Any]:
        def query(session: sqlalchemy.orm.scoping.scoped_session) -> None:
            result = session.query(model).first()
            if result is None:
                raise HTTPNotFound(model.__name__ + " record not found")

        return query


def _maybe_function(what: Any, request: pyramid.request.Request) -> Any:
    return what(request) if callable(what) else what


@broadcast.decorator(expect_answers=True)
def _get_all_versions() -> Optional[str]:
    return version.get_version()
