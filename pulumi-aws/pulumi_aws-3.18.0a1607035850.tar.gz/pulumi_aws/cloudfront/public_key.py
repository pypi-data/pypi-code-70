# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['PublicKey']


class PublicKey(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 encoded_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Example Usage

        The following example below creates a CloudFront public key.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloudfront.PublicKey("example",
            comment="test public key",
            encoded_key=(lambda path: open(path).read())("public_key.pem"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: An optional comment about the public key.
        :param pulumi.Input[str] encoded_key: The encoded public key that you want to add to CloudFront to use with features like field-level encryption.
        :param pulumi.Input[str] name: The name for the public key. By default generated by this provider.
        :param pulumi.Input[str] name_prefix: The name for the public key. Conflicts with `name`.
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

            __props__['comment'] = comment
            if encoded_key is None and not opts.urn:
                raise TypeError("Missing required property 'encoded_key'")
            __props__['encoded_key'] = encoded_key
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['caller_reference'] = None
            __props__['etag'] = None
        super(PublicKey, __self__).__init__(
            'aws:cloudfront/publicKey:PublicKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            caller_reference: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            encoded_key: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None) -> 'PublicKey':
        """
        Get an existing PublicKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] caller_reference: Internal value used by CloudFront to allow future updates to the public key configuration.
        :param pulumi.Input[str] comment: An optional comment about the public key.
        :param pulumi.Input[str] encoded_key: The encoded public key that you want to add to CloudFront to use with features like field-level encryption.
        :param pulumi.Input[str] etag: The current version of the public key. For example: `E2QWRUHAPOMQZL`.
        :param pulumi.Input[str] name: The name for the public key. By default generated by this provider.
        :param pulumi.Input[str] name_prefix: The name for the public key. Conflicts with `name`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["caller_reference"] = caller_reference
        __props__["comment"] = comment
        __props__["encoded_key"] = encoded_key
        __props__["etag"] = etag
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        return PublicKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> pulumi.Output[str]:
        """
        Internal value used by CloudFront to allow future updates to the public key configuration.
        """
        return pulumi.get(self, "caller_reference")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        An optional comment about the public key.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="encodedKey")
    def encoded_key(self) -> pulumi.Output[str]:
        """
        The encoded public key that you want to add to CloudFront to use with features like field-level encryption.
        """
        return pulumi.get(self, "encoded_key")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The current version of the public key. For example: `E2QWRUHAPOMQZL`.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for the public key. By default generated by this provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[str]:
        """
        The name for the public key. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

