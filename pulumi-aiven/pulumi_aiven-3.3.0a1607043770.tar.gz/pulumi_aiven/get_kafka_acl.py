# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetKafkaAclResult',
    'AwaitableGetKafkaAclResult',
    'get_kafka_acl',
]

@pulumi.output_type
class GetKafkaAclResult:
    """
    A collection of values returned by getKafkaAcl.
    """
    def __init__(__self__, id=None, permission=None, project=None, service_name=None, topic=None, username=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if permission and not isinstance(permission, str):
            raise TypeError("Expected argument 'permission' to be a str")
        pulumi.set(__self__, "permission", permission)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if topic and not isinstance(topic, str):
            raise TypeError("Expected argument 'topic' to be a str")
        pulumi.set(__self__, "topic", topic)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def permission(self) -> str:
        return pulumi.get(self, "permission")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def topic(self) -> str:
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")


class AwaitableGetKafkaAclResult(GetKafkaAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaAclResult(
            id=self.id,
            permission=self.permission,
            project=self.project,
            service_name=self.service_name,
            topic=self.topic,
            username=self.username)


def get_kafka_acl(permission: Optional[str] = None,
                  project: Optional[str] = None,
                  service_name: Optional[str] = None,
                  topic: Optional[str] = None,
                  username: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaAclResult:
    """
    ## # Data Source Kafka ACL Data Source

    The Data Source Kafka ACL data source provides information about the existing Aiven Kafka ACL
    for a Kafka service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    mytestacl = aiven.get_kafka_acl(permission="admin",
        project=aiven_project["myproject"]["project"],
        service_name=aiven_service["myservice"]["service_name"],
        topic="<TOPIC_NAME_PATTERN>",
        username="<USERNAME_PATTERN>")
    ```


    :param str permission: is the level of permission the matching users are given to the matching
           topics (admin, read, readwrite, write).
    :param str project: and `service_name` - (Required) define the project and service the ACL belongs to.
           They should be defined using reference as shown above to set up dependencies correctly.
           These properties cannot be changed once the service is created. Doing so will result in
           the topic being deleted and new one created instead.
    :param str topic: is a topic name pattern the ACL entry matches to.
    :param str username: is a username pattern the ACL entry matches to.
    """
    __args__ = dict()
    __args__['permission'] = permission
    __args__['project'] = project
    __args__['serviceName'] = service_name
    __args__['topic'] = topic
    __args__['username'] = username
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aiven:index/getKafkaAcl:getKafkaAcl', __args__, opts=opts, typ=GetKafkaAclResult).value

    return AwaitableGetKafkaAclResult(
        id=__ret__.id,
        permission=__ret__.permission,
        project=__ret__.project,
        service_name=__ret__.service_name,
        topic=__ret__.topic,
        username=__ret__.username)
