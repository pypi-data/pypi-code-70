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

__all__ = ['KafkaConnector']


class KafkaConnector(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # Kafka connectors Resource

        The Kafka connectors resource allows the creation and management of an Aiven Kafka connectors.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        kafka_es_con1 = aiven.KafkaConnector("kafka-es-con1",
            project=aiven_project["kafka-con-project1"]["project"],
            service_name=aiven_service["kafka-service1"]["service_name"],
            connector_name="kafka-es-con1",
            config={
                "topics": aiven_kafka_topic["kafka-topic1"]["topic_name"],
                "connector.class": "io.aiven.connect.elasticsearch.ElasticsearchSinkConnector",
                "type.name": "es-connector",
                "name": "kafka-es-con1",
                "connection.url": aiven_service["es-service1"]["service_uri"],
            })
        ```

        * `project` and `service_name`- (Required) define the project and service the Kafka Connectors belongs to.
        They should be defined using reference as shown above to set up dependencies correctly.

        * `connector_name`- (Required) is the Kafka connector name.

        * `config`- (Required)is the Kafka Connector configuration parameters, where `topics`, `connector.class` and `name`
        are required parameters but the rest of them are connector type specific.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: Kafka Connector configuration parameters
        :param pulumi.Input[str] connector_name: Kafka connector name
        :param pulumi.Input[str] project: Project to link the kafka connector to
        :param pulumi.Input[str] service_name: Service to link the kafka connector to
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

            if config is None:
                raise TypeError("Missing required property 'config'")
            __props__['config'] = config
            if connector_name is None:
                raise TypeError("Missing required property 'connector_name'")
            __props__['connector_name'] = connector_name
            if project is None:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            if service_name is None:
                raise TypeError("Missing required property 'service_name'")
            __props__['service_name'] = service_name
            __props__['plugin_author'] = None
            __props__['plugin_class'] = None
            __props__['plugin_doc_url'] = None
            __props__['plugin_title'] = None
            __props__['plugin_type'] = None
            __props__['plugin_version'] = None
            __props__['tasks'] = None
        super(KafkaConnector, __self__).__init__(
            'aiven:index/kafkaConnector:KafkaConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            connector_name: Optional[pulumi.Input[str]] = None,
            plugin_author: Optional[pulumi.Input[str]] = None,
            plugin_class: Optional[pulumi.Input[str]] = None,
            plugin_doc_url: Optional[pulumi.Input[str]] = None,
            plugin_title: Optional[pulumi.Input[str]] = None,
            plugin_type: Optional[pulumi.Input[str]] = None,
            plugin_version: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            tasks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaConnectorTaskArgs']]]]] = None) -> 'KafkaConnector':
        """
        Get an existing KafkaConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: Kafka Connector configuration parameters
        :param pulumi.Input[str] connector_name: Kafka connector name
        :param pulumi.Input[str] plugin_author: Kafka connector author.
        :param pulumi.Input[str] plugin_class: Kafka connector Java class.
        :param pulumi.Input[str] plugin_doc_url: Kafka connector documentation URL.
        :param pulumi.Input[str] plugin_title: Kafka connector title.
        :param pulumi.Input[str] plugin_type: Kafka connector type.
        :param pulumi.Input[str] plugin_version: Kafka connector version.
        :param pulumi.Input[str] project: Project to link the kafka connector to
        :param pulumi.Input[str] service_name: Service to link the kafka connector to
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaConnectorTaskArgs']]]] tasks: List of tasks of a connector, each element contains `connector` 
               (Related connector name) and `task` (Task id / number).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["config"] = config
        __props__["connector_name"] = connector_name
        __props__["plugin_author"] = plugin_author
        __props__["plugin_class"] = plugin_class
        __props__["plugin_doc_url"] = plugin_doc_url
        __props__["plugin_title"] = plugin_title
        __props__["plugin_type"] = plugin_type
        __props__["plugin_version"] = plugin_version
        __props__["project"] = project
        __props__["service_name"] = service_name
        __props__["tasks"] = tasks
        return KafkaConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Kafka Connector configuration parameters
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Output[str]:
        """
        Kafka connector name
        """
        return pulumi.get(self, "connector_name")

    @property
    @pulumi.getter(name="pluginAuthor")
    def plugin_author(self) -> pulumi.Output[str]:
        """
        Kafka connector author.
        """
        return pulumi.get(self, "plugin_author")

    @property
    @pulumi.getter(name="pluginClass")
    def plugin_class(self) -> pulumi.Output[str]:
        """
        Kafka connector Java class.
        """
        return pulumi.get(self, "plugin_class")

    @property
    @pulumi.getter(name="pluginDocUrl")
    def plugin_doc_url(self) -> pulumi.Output[str]:
        """
        Kafka connector documentation URL.
        """
        return pulumi.get(self, "plugin_doc_url")

    @property
    @pulumi.getter(name="pluginTitle")
    def plugin_title(self) -> pulumi.Output[str]:
        """
        Kafka connector title.
        """
        return pulumi.get(self, "plugin_title")

    @property
    @pulumi.getter(name="pluginType")
    def plugin_type(self) -> pulumi.Output[str]:
        """
        Kafka connector type.
        """
        return pulumi.get(self, "plugin_type")

    @property
    @pulumi.getter(name="pluginVersion")
    def plugin_version(self) -> pulumi.Output[str]:
        """
        Kafka connector version.
        """
        return pulumi.get(self, "plugin_version")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        Project to link the kafka connector to
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        Service to link the kafka connector to
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def tasks(self) -> pulumi.Output[Sequence['outputs.KafkaConnectorTask']]:
        """
        List of tasks of a connector, each element contains `connector` 
        (Related connector name) and `task` (Task id / number).
        """
        return pulumi.get(self, "tasks")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

