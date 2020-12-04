# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['OpenIdConnectProvider']


class OpenIdConnectProvider(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 thumbprint_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an IAM OpenID Connect provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        default = aws.iam.OpenIdConnectProvider("default",
            client_id_lists=["266362248691-342342xasdasdasda-apps.googleusercontent.com"],
            thumbprint_lists=[],
            url="https://accounts.google.com")
        ```

        ## Import

        IAM OpenID Connect Providers can be imported using the `arn`, e.g.

        ```sh
         $ pulumi import aws:iam/openIdConnectProvider:OpenIdConnectProvider default arn:aws:iam::123456789012:oidc-provider/accounts.google.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_id_lists: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] thumbprint_lists: A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).
        :param pulumi.Input[str] url: The URL of the identity provider. Corresponds to the _iss_ claim.
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

            if client_id_lists is None and not opts.urn:
                raise TypeError("Missing required property 'client_id_lists'")
            __props__['client_id_lists'] = client_id_lists
            if thumbprint_lists is None and not opts.urn:
                raise TypeError("Missing required property 'thumbprint_lists'")
            __props__['thumbprint_lists'] = thumbprint_lists
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__['url'] = url
            __props__['arn'] = None
        super(OpenIdConnectProvider, __self__).__init__(
            'aws:iam/openIdConnectProvider:OpenIdConnectProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            client_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            thumbprint_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'OpenIdConnectProvider':
        """
        Get an existing OpenIdConnectProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN assigned by AWS for this provider.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_id_lists: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] thumbprint_lists: A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).
        :param pulumi.Input[str] url: The URL of the identity provider. Corresponds to the _iss_ claim.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["client_id_lists"] = client_id_lists
        __props__["thumbprint_lists"] = thumbprint_lists
        __props__["url"] = url
        return OpenIdConnectProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN assigned by AWS for this provider.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clientIdLists")
    def client_id_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)
        """
        return pulumi.get(self, "client_id_lists")

    @property
    @pulumi.getter(name="thumbprintLists")
    def thumbprint_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).
        """
        return pulumi.get(self, "thumbprint_lists")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the identity provider. Corresponds to the _iss_ claim.
        """
        return pulumi.get(self, "url")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

