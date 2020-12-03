# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Deployment']


class Deployment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Amazon API Gateway Version 2 deployment.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

        > **Note:** Creating a deployment for an API requires at least one `apigatewayv2.Route` resource associated with that API. To avoid race conditions when all resources are being created together, you need to add implicit resource references via the `triggers` argument or explicit resource references using the [resource `dependsOn` meta-argument](https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson).

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.Deployment("example",
            api_id=aws_apigatewayv2_route["example"]["api_id"],
            description="Example deployment")
        ```

        ## Import

        `aws_apigatewayv2_deployment` can be imported by using the API identifier and deployment identifier, e.g.

        ```sh
         $ pulumi import aws:apigatewayv2/deployment:Deployment example aabbccddee/1122334
        ```

         The `triggers` argument cannot be imported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] description: The description for the deployment resource. Must be less than or equal to 1024 characters in length.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: A map of arbitrary keys and values that, when changed, will trigger a redeployment.
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

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            __props__['description'] = description
            __props__['triggers'] = triggers
            __props__['auto_deployed'] = None
        super(Deployment, __self__).__init__(
            'aws:apigatewayv2/deployment:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_id: Optional[pulumi.Input[str]] = None,
            auto_deployed: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[bool] auto_deployed: Whether the deployment was automatically released.
        :param pulumi.Input[str] description: The description for the deployment resource. Must be less than or equal to 1024 characters in length.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: A map of arbitrary keys and values that, when changed, will trigger a redeployment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["auto_deployed"] = auto_deployed
        __props__["description"] = description
        __props__["triggers"] = triggers
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="autoDeployed")
    def auto_deployed(self) -> pulumi.Output[bool]:
        """
        Whether the deployment was automatically released.
        """
        return pulumi.get(self, "auto_deployed")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description for the deployment resource. Must be less than or equal to 1024 characters in length.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of arbitrary keys and values that, when changed, will trigger a redeployment.
        """
        return pulumi.get(self, "triggers")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

