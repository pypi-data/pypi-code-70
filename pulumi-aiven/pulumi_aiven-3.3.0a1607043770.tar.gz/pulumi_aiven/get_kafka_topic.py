# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetKafkaTopicResult',
    'AwaitableGetKafkaTopicResult',
    'get_kafka_topic',
]

@pulumi.output_type
class GetKafkaTopicResult:
    """
    A collection of values returned by getKafkaTopic.
    """
    def __init__(__self__, cleanup_policy=None, config=None, id=None, minimum_in_sync_replicas=None, partitions=None, project=None, replication=None, retention_bytes=None, retention_hours=None, service_name=None, termination_protection=None, topic_name=None):
        if cleanup_policy and not isinstance(cleanup_policy, str):
            raise TypeError("Expected argument 'cleanup_policy' to be a str")
        pulumi.set(__self__, "cleanup_policy", cleanup_policy)
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if minimum_in_sync_replicas and not isinstance(minimum_in_sync_replicas, int):
            raise TypeError("Expected argument 'minimum_in_sync_replicas' to be a int")
        pulumi.set(__self__, "minimum_in_sync_replicas", minimum_in_sync_replicas)
        if partitions and not isinstance(partitions, int):
            raise TypeError("Expected argument 'partitions' to be a int")
        pulumi.set(__self__, "partitions", partitions)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if replication and not isinstance(replication, int):
            raise TypeError("Expected argument 'replication' to be a int")
        pulumi.set(__self__, "replication", replication)
        if retention_bytes and not isinstance(retention_bytes, int):
            raise TypeError("Expected argument 'retention_bytes' to be a int")
        pulumi.set(__self__, "retention_bytes", retention_bytes)
        if retention_hours and not isinstance(retention_hours, int):
            raise TypeError("Expected argument 'retention_hours' to be a int")
        pulumi.set(__self__, "retention_hours", retention_hours)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if termination_protection and not isinstance(termination_protection, bool):
            raise TypeError("Expected argument 'termination_protection' to be a bool")
        pulumi.set(__self__, "termination_protection", termination_protection)
        if topic_name and not isinstance(topic_name, str):
            raise TypeError("Expected argument 'topic_name' to be a str")
        pulumi.set(__self__, "topic_name", topic_name)

    @property
    @pulumi.getter(name="cleanupPolicy")
    def cleanup_policy(self) -> Optional[str]:
        """
        cleanup.policy value
        """
        return pulumi.get(self, "cleanup_policy")

    @property
    @pulumi.getter
    def config(self) -> Optional['outputs.GetKafkaTopicConfigResult']:
        """
        Kafka topic configuration
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="minimumInSyncReplicas")
    def minimum_in_sync_replicas(self) -> Optional[int]:
        """
        Minimum required nodes in-sync replicas (ISR) to produce to a partition.
        """
        return pulumi.get(self, "minimum_in_sync_replicas")

    @property
    @pulumi.getter
    def partitions(self) -> Optional[int]:
        """
        Number of partitions to create in the topic.
        """
        return pulumi.get(self, "partitions")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def replication(self) -> Optional[int]:
        """
        Replication factor for the topic.
        """
        return pulumi.get(self, "replication")

    @property
    @pulumi.getter(name="retentionBytes")
    def retention_bytes(self) -> Optional[int]:
        """
        retention.bytes value
        """
        return pulumi.get(self, "retention_bytes")

    @property
    @pulumi.getter(name="retentionHours")
    def retention_hours(self) -> Optional[int]:
        """
        Retention period in hours, if -1 it is infinite.
        """
        return pulumi.get(self, "retention_hours")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> Optional[bool]:
        return pulumi.get(self, "termination_protection")

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> str:
        return pulumi.get(self, "topic_name")


class AwaitableGetKafkaTopicResult(GetKafkaTopicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaTopicResult(
            cleanup_policy=self.cleanup_policy,
            config=self.config,
            id=self.id,
            minimum_in_sync_replicas=self.minimum_in_sync_replicas,
            partitions=self.partitions,
            project=self.project,
            replication=self.replication,
            retention_bytes=self.retention_bytes,
            retention_hours=self.retention_hours,
            service_name=self.service_name,
            termination_protection=self.termination_protection,
            topic_name=self.topic_name)


def get_kafka_topic(cleanup_policy: Optional[str] = None,
                    config: Optional[pulumi.InputType['GetKafkaTopicConfigArgs']] = None,
                    minimum_in_sync_replicas: Optional[int] = None,
                    partitions: Optional[int] = None,
                    project: Optional[str] = None,
                    replication: Optional[int] = None,
                    retention_bytes: Optional[int] = None,
                    retention_hours: Optional[int] = None,
                    service_name: Optional[str] = None,
                    termination_protection: Optional[bool] = None,
                    topic_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaTopicResult:
    """
    ## # Kafka Topic Data Source

    The Kafka Topic data source provides information about the existing Aiven Kafka Topic.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    mytesttopic = aiven.get_kafka_topic(config=aiven.GetKafkaTopicConfigArgs(
            cleanup_policy="compact",
            flush_ms="10",
            unclean_leader_election_enable="true",
        ),
        partitions=3,
        project=aiven_project["myproject"]["project"],
        replication=1,
        service_name=aiven_service["myservice"]["service_name"],
        topic_name="<TOPIC_NAME>")
    ```


    :param str cleanup_policy: cleanup.policy value
    :param pulumi.InputType['GetKafkaTopicConfigArgs'] config: Kafka topic configuration
    :param int minimum_in_sync_replicas: Minimum required nodes in-sync replicas (ISR) to produce to a partition.
    :param int partitions: Number of partitions to create in the topic.
    :param str project: and `service_name` - (Required) define the project and service the topic belongs to.
           They should be defined using reference as shown above to set up dependencies correctly.
           These properties cannot be changed once the service is created. Doing so will result in
           the topic being deleted and new one created instead.
    :param int replication: Replication factor for the topic.
    :param int retention_bytes: retention.bytes value
    :param int retention_hours: Retention period in hours, if -1 it is infinite.
    :param str topic_name: is the actual name of the topic account. This propery cannot be changed
           once the service is created. Doing so will result in the topic being deleted and new one
           created instead.
    """
    __args__ = dict()
    __args__['cleanupPolicy'] = cleanup_policy
    __args__['config'] = config
    __args__['minimumInSyncReplicas'] = minimum_in_sync_replicas
    __args__['partitions'] = partitions
    __args__['project'] = project
    __args__['replication'] = replication
    __args__['retentionBytes'] = retention_bytes
    __args__['retentionHours'] = retention_hours
    __args__['serviceName'] = service_name
    __args__['terminationProtection'] = termination_protection
    __args__['topicName'] = topic_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aiven:index/getKafkaTopic:getKafkaTopic', __args__, opts=opts, typ=GetKafkaTopicResult).value

    return AwaitableGetKafkaTopicResult(
        cleanup_policy=__ret__.cleanup_policy,
        config=__ret__.config,
        id=__ret__.id,
        minimum_in_sync_replicas=__ret__.minimum_in_sync_replicas,
        partitions=__ret__.partitions,
        project=__ret__.project,
        replication=__ret__.replication,
        retention_bytes=__ret__.retention_bytes,
        retention_hours=__ret__.retention_hours,
        service_name=__ret__.service_name,
        termination_protection=__ret__.termination_protection,
        topic_name=__ret__.topic_name)
