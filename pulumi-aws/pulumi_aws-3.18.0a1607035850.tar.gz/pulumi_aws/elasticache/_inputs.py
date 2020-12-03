# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterCacheNodeArgs',
    'ParameterGroupParameterArgs',
    'ReplicationGroupClusterModeArgs',
]

@pulumi.input_type
class ClusterCacheNodeArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] availability_zone: The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
        :param pulumi.Input[int] port: The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)


@pulumi.input_type
class ParameterGroupParameterArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the ElastiCache parameter.
        :param pulumi.Input[str] value: The value of the ElastiCache parameter.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the ElastiCache parameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the ElastiCache parameter.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ReplicationGroupClusterModeArgs:
    def __init__(__self__, *,
                 num_node_groups: pulumi.Input[int],
                 replicas_per_node_group: pulumi.Input[int]):
        """
        :param pulumi.Input[int] num_node_groups: Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.
        :param pulumi.Input[int] replicas_per_node_group: Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.
        """
        pulumi.set(__self__, "num_node_groups", num_node_groups)
        pulumi.set(__self__, "replicas_per_node_group", replicas_per_node_group)

    @property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> pulumi.Input[int]:
        """
        Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.
        """
        return pulumi.get(self, "num_node_groups")

    @num_node_groups.setter
    def num_node_groups(self, value: pulumi.Input[int]):
        pulumi.set(self, "num_node_groups", value)

    @property
    @pulumi.getter(name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> pulumi.Input[int]:
        """
        Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.
        """
        return pulumi.get(self, "replicas_per_node_group")

    @replicas_per_node_group.setter
    def replicas_per_node_group(self, value: pulumi.Input[int]):
        pulumi.set(self, "replicas_per_node_group", value)


