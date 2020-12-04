# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ClusterSnapshot']


class ClusterSnapshot(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 db_cluster_snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Neptune database cluster snapshot.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.neptune.ClusterSnapshot("example",
            db_cluster_identifier=aws_neptune_cluster["example"]["id"],
            db_cluster_snapshot_identifier="resourcetestsnapshot1234")
        ```

        ## Import

        `aws_neptune_cluster_snapshot` can be imported by using the cluster snapshot identifier, e.g.

        ```sh
         $ pulumi import aws:neptune/clusterSnapshot:ClusterSnapshot example my-cluster-snapshot
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_cluster_identifier: The DB Cluster Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_cluster_snapshot_identifier: The Identifier for the snapshot.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if db_cluster_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'db_cluster_identifier'")
            __props__['db_cluster_identifier'] = db_cluster_identifier
            if db_cluster_snapshot_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'db_cluster_snapshot_identifier'")
            __props__['db_cluster_snapshot_identifier'] = db_cluster_snapshot_identifier
            __props__['allocated_storage'] = None
            __props__['availability_zones'] = None
            __props__['db_cluster_snapshot_arn'] = None
            __props__['engine'] = None
            __props__['engine_version'] = None
            __props__['kms_key_id'] = None
            __props__['license_model'] = None
            __props__['port'] = None
            __props__['snapshot_type'] = None
            __props__['source_db_cluster_snapshot_arn'] = None
            __props__['status'] = None
            __props__['storage_encrypted'] = None
            __props__['vpc_id'] = None
        super(ClusterSnapshot, __self__).__init__(
            'aws:neptune/clusterSnapshot:ClusterSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocated_storage: Optional[pulumi.Input[int]] = None,
            availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            db_cluster_identifier: Optional[pulumi.Input[str]] = None,
            db_cluster_snapshot_arn: Optional[pulumi.Input[str]] = None,
            db_cluster_snapshot_identifier: Optional[pulumi.Input[str]] = None,
            engine: Optional[pulumi.Input[str]] = None,
            engine_version: Optional[pulumi.Input[str]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            license_model: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            snapshot_type: Optional[pulumi.Input[str]] = None,
            source_db_cluster_snapshot_arn: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            storage_encrypted: Optional[pulumi.Input[bool]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'ClusterSnapshot':
        """
        Get an existing ClusterSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] allocated_storage: Specifies the allocated storage size in gigabytes (GB).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
        :param pulumi.Input[str] db_cluster_identifier: The DB Cluster Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_cluster_snapshot_arn: The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
        :param pulumi.Input[str] db_cluster_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[str] engine: Specifies the name of the database engine.
        :param pulumi.Input[str] engine_version: Version of the database engine for this DB cluster snapshot.
        :param pulumi.Input[str] kms_key_id: If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
        :param pulumi.Input[str] license_model: License model information for the restored DB cluster.
        :param pulumi.Input[int] port: Port that the DB cluster was listening on at the time of the snapshot.
        :param pulumi.Input[str] status: The status of this DB Cluster Snapshot.
        :param pulumi.Input[bool] storage_encrypted: Specifies whether the DB cluster snapshot is encrypted.
        :param pulumi.Input[str] vpc_id: The VPC ID associated with the DB cluster snapshot.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allocated_storage"] = allocated_storage
        __props__["availability_zones"] = availability_zones
        __props__["db_cluster_identifier"] = db_cluster_identifier
        __props__["db_cluster_snapshot_arn"] = db_cluster_snapshot_arn
        __props__["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier
        __props__["engine"] = engine
        __props__["engine_version"] = engine_version
        __props__["kms_key_id"] = kms_key_id
        __props__["license_model"] = license_model
        __props__["port"] = port
        __props__["snapshot_type"] = snapshot_type
        __props__["source_db_cluster_snapshot_arn"] = source_db_cluster_snapshot_arn
        __props__["status"] = status
        __props__["storage_encrypted"] = storage_encrypted
        __props__["vpc_id"] = vpc_id
        return ClusterSnapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[int]:
        """
        Specifies the allocated storage size in gigabytes (GB).
        """
        return pulumi.get(self, "allocated_storage")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[str]]:
        """
        List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> pulumi.Output[str]:
        """
        The DB Cluster Identifier from which to take the snapshot.
        """
        return pulumi.get(self, "db_cluster_identifier")

    @property
    @pulumi.getter(name="dbClusterSnapshotArn")
    def db_cluster_snapshot_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
        """
        return pulumi.get(self, "db_cluster_snapshot_arn")

    @property
    @pulumi.getter(name="dbClusterSnapshotIdentifier")
    def db_cluster_snapshot_identifier(self) -> pulumi.Output[str]:
        """
        The Identifier for the snapshot.
        """
        return pulumi.get(self, "db_cluster_snapshot_identifier")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        Specifies the name of the database engine.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[str]:
        """
        Version of the database engine for this DB cluster snapshot.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[str]:
        """
        If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Output[str]:
        """
        License model information for the restored DB cluster.
        """
        return pulumi.get(self, "license_model")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Port that the DB cluster was listening on at the time of the snapshot.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "snapshot_type")

    @property
    @pulumi.getter(name="sourceDbClusterSnapshotArn")
    def source_db_cluster_snapshot_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_db_cluster_snapshot_arn")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of this DB Cluster Snapshot.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[bool]:
        """
        Specifies whether the DB cluster snapshot is encrypted.
        """
        return pulumi.get(self, "storage_encrypted")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The VPC ID associated with the DB cluster snapshot.
        """
        return pulumi.get(self, "vpc_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

