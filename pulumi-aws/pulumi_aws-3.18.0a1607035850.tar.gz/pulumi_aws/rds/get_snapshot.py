# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetSnapshotResult',
    'AwaitableGetSnapshotResult',
    'get_snapshot',
]

@pulumi.output_type
class GetSnapshotResult:
    """
    A collection of values returned by getSnapshot.
    """
    def __init__(__self__, allocated_storage=None, availability_zone=None, db_instance_identifier=None, db_snapshot_arn=None, db_snapshot_identifier=None, encrypted=None, engine=None, engine_version=None, id=None, include_public=None, include_shared=None, iops=None, kms_key_id=None, license_model=None, most_recent=None, option_group_name=None, port=None, snapshot_create_time=None, snapshot_type=None, source_db_snapshot_identifier=None, source_region=None, status=None, storage_type=None, vpc_id=None):
        if allocated_storage and not isinstance(allocated_storage, int):
            raise TypeError("Expected argument 'allocated_storage' to be a int")
        pulumi.set(__self__, "allocated_storage", allocated_storage)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if db_instance_identifier and not isinstance(db_instance_identifier, str):
            raise TypeError("Expected argument 'db_instance_identifier' to be a str")
        pulumi.set(__self__, "db_instance_identifier", db_instance_identifier)
        if db_snapshot_arn and not isinstance(db_snapshot_arn, str):
            raise TypeError("Expected argument 'db_snapshot_arn' to be a str")
        pulumi.set(__self__, "db_snapshot_arn", db_snapshot_arn)
        if db_snapshot_identifier and not isinstance(db_snapshot_identifier, str):
            raise TypeError("Expected argument 'db_snapshot_identifier' to be a str")
        pulumi.set(__self__, "db_snapshot_identifier", db_snapshot_identifier)
        if encrypted and not isinstance(encrypted, bool):
            raise TypeError("Expected argument 'encrypted' to be a bool")
        pulumi.set(__self__, "encrypted", encrypted)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_public and not isinstance(include_public, bool):
            raise TypeError("Expected argument 'include_public' to be a bool")
        pulumi.set(__self__, "include_public", include_public)
        if include_shared and not isinstance(include_shared, bool):
            raise TypeError("Expected argument 'include_shared' to be a bool")
        pulumi.set(__self__, "include_shared", include_shared)
        if iops and not isinstance(iops, int):
            raise TypeError("Expected argument 'iops' to be a int")
        pulumi.set(__self__, "iops", iops)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if license_model and not isinstance(license_model, str):
            raise TypeError("Expected argument 'license_model' to be a str")
        pulumi.set(__self__, "license_model", license_model)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if option_group_name and not isinstance(option_group_name, str):
            raise TypeError("Expected argument 'option_group_name' to be a str")
        pulumi.set(__self__, "option_group_name", option_group_name)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if snapshot_create_time and not isinstance(snapshot_create_time, str):
            raise TypeError("Expected argument 'snapshot_create_time' to be a str")
        pulumi.set(__self__, "snapshot_create_time", snapshot_create_time)
        if snapshot_type and not isinstance(snapshot_type, str):
            raise TypeError("Expected argument 'snapshot_type' to be a str")
        pulumi.set(__self__, "snapshot_type", snapshot_type)
        if source_db_snapshot_identifier and not isinstance(source_db_snapshot_identifier, str):
            raise TypeError("Expected argument 'source_db_snapshot_identifier' to be a str")
        pulumi.set(__self__, "source_db_snapshot_identifier", source_db_snapshot_identifier)
        if source_region and not isinstance(source_region, str):
            raise TypeError("Expected argument 'source_region' to be a str")
        pulumi.set(__self__, "source_region", source_region)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> int:
        """
        Specifies the allocated storage size in gigabytes (GB).
        """
        return pulumi.get(self, "allocated_storage")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> Optional[str]:
        return pulumi.get(self, "db_instance_identifier")

    @property
    @pulumi.getter(name="dbSnapshotArn")
    def db_snapshot_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) for the DB snapshot.
        """
        return pulumi.get(self, "db_snapshot_arn")

    @property
    @pulumi.getter(name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> Optional[str]:
        return pulumi.get(self, "db_snapshot_identifier")

    @property
    @pulumi.getter
    def encrypted(self) -> bool:
        """
        Specifies whether the DB snapshot is encrypted.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        Specifies the name of the database engine.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        """
        Specifies the version of the database engine.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includePublic")
    def include_public(self) -> Optional[bool]:
        return pulumi.get(self, "include_public")

    @property
    @pulumi.getter(name="includeShared")
    def include_shared(self) -> Optional[bool]:
        return pulumi.get(self, "include_shared")

    @property
    @pulumi.getter
    def iops(self) -> int:
        """
        Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
        """
        return pulumi.get(self, "iops")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        The ARN for the KMS encryption key.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> str:
        """
        License model information for the restored DB instance.
        """
        return pulumi.get(self, "license_model")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> str:
        """
        Provides the option group name for the DB snapshot.
        """
        return pulumi.get(self, "option_group_name")

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="snapshotCreateTime")
    def snapshot_create_time(self) -> str:
        """
        Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
        """
        return pulumi.get(self, "snapshot_create_time")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[str]:
        return pulumi.get(self, "snapshot_type")

    @property
    @pulumi.getter(name="sourceDbSnapshotIdentifier")
    def source_db_snapshot_identifier(self) -> str:
        """
        The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
        """
        return pulumi.get(self, "source_db_snapshot_identifier")

    @property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> str:
        """
        The region that the DB snapshot was created in or copied from.
        """
        return pulumi.get(self, "source_region")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Specifies the status of this DB snapshot.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        """
        Specifies the storage type associated with DB snapshot.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        Specifies the ID of the VPC associated with the DB snapshot.
        """
        return pulumi.get(self, "vpc_id")


class AwaitableGetSnapshotResult(GetSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotResult(
            allocated_storage=self.allocated_storage,
            availability_zone=self.availability_zone,
            db_instance_identifier=self.db_instance_identifier,
            db_snapshot_arn=self.db_snapshot_arn,
            db_snapshot_identifier=self.db_snapshot_identifier,
            encrypted=self.encrypted,
            engine=self.engine,
            engine_version=self.engine_version,
            id=self.id,
            include_public=self.include_public,
            include_shared=self.include_shared,
            iops=self.iops,
            kms_key_id=self.kms_key_id,
            license_model=self.license_model,
            most_recent=self.most_recent,
            option_group_name=self.option_group_name,
            port=self.port,
            snapshot_create_time=self.snapshot_create_time,
            snapshot_type=self.snapshot_type,
            source_db_snapshot_identifier=self.source_db_snapshot_identifier,
            source_region=self.source_region,
            status=self.status,
            storage_type=self.storage_type,
            vpc_id=self.vpc_id)


def get_snapshot(db_instance_identifier: Optional[str] = None,
                 db_snapshot_identifier: Optional[str] = None,
                 include_public: Optional[bool] = None,
                 include_shared: Optional[bool] = None,
                 most_recent: Optional[bool] = None,
                 snapshot_type: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotResult:
    """
    Use this data source to get information about a DB Snapshot for use when provisioning DB instances

    > **NOTE:** This data source does not apply to snapshots created on Aurora DB clusters.
    See the `rds.ClusterSnapshot` data source for DB Cluster snapshots.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    prod = aws.rds.Instance("prod",
        allocated_storage=10,
        engine="mysql",
        engine_version="5.6.17",
        instance_class="db.t2.micro",
        name="mydb",
        username="foo",
        password="bar",
        db_subnet_group_name="my_database_subnet_group",
        parameter_group_name="default.mysql5.6")
    latest_prod_snapshot = prod.id.apply(lambda id: aws.rds.get_snapshot(db_instance_identifier=id,
        most_recent=True))
    # Use the latest production snapshot to create a dev instance.
    dev = aws.rds.Instance("dev",
        instance_class="db.t2.micro",
        name="mydbdev",
        snapshot_identifier=latest_prod_snapshot.id)
    ```


    :param str db_instance_identifier: Returns the list of snapshots created by the specific db_instance
    :param str db_snapshot_identifier: Returns information on a specific snapshot_id.
    :param bool include_public: Set this value to true to include manual DB snapshots that are public and can be
           copied or restored by any AWS account, otherwise set this value to false. The default is `false`.
    :param bool include_shared: Set this value to true to include shared manual DB snapshots from other
           AWS accounts that this AWS account has been given permission to copy or restore, otherwise set this value to false.
           The default is `false`.
    :param bool most_recent: If more than one result is returned, use the most
           recent Snapshot.
    :param str snapshot_type: The type of snapshots to be returned. If you don't specify a SnapshotType
           value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not
           included in the returned results by default. Possible values are, `automated`, `manual`, `shared` and `public`.
    """
    __args__ = dict()
    __args__['dbInstanceIdentifier'] = db_instance_identifier
    __args__['dbSnapshotIdentifier'] = db_snapshot_identifier
    __args__['includePublic'] = include_public
    __args__['includeShared'] = include_shared
    __args__['mostRecent'] = most_recent
    __args__['snapshotType'] = snapshot_type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:rds/getSnapshot:getSnapshot', __args__, opts=opts, typ=GetSnapshotResult).value

    return AwaitableGetSnapshotResult(
        allocated_storage=__ret__.allocated_storage,
        availability_zone=__ret__.availability_zone,
        db_instance_identifier=__ret__.db_instance_identifier,
        db_snapshot_arn=__ret__.db_snapshot_arn,
        db_snapshot_identifier=__ret__.db_snapshot_identifier,
        encrypted=__ret__.encrypted,
        engine=__ret__.engine,
        engine_version=__ret__.engine_version,
        id=__ret__.id,
        include_public=__ret__.include_public,
        include_shared=__ret__.include_shared,
        iops=__ret__.iops,
        kms_key_id=__ret__.kms_key_id,
        license_model=__ret__.license_model,
        most_recent=__ret__.most_recent,
        option_group_name=__ret__.option_group_name,
        port=__ret__.port,
        snapshot_create_time=__ret__.snapshot_create_time,
        snapshot_type=__ret__.snapshot_type,
        source_db_snapshot_identifier=__ret__.source_db_snapshot_identifier,
        source_region=__ret__.source_region,
        status=__ret__.status,
        storage_type=__ret__.storage_type,
        vpc_id=__ret__.vpc_id)
