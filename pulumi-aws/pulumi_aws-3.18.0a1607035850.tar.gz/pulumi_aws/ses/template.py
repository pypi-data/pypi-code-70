# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Template']


class Template(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 html: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to create a SES template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        my_template = aws.ses.Template("myTemplate",
            html="<h1>Hello {{name}},</h1><p>Your favorite animal is {{favoriteanimal}}.</p>",
            subject="Greetings, {{name}}!",
            text=\"\"\"Hello {{name}},
        Your favorite animal is {{favoriteanimal}}.
        \"\"\")
        ```

        ## Import

        SES templates can be imported using the template name, e.g.

        ```sh
         $ pulumi import aws:ses/template:Template MyTemplate MyTemplate
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] html: The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        :param pulumi.Input[str] name: The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        :param pulumi.Input[str] subject: The subject line of the email.
        :param pulumi.Input[str] text: The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
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

            __props__['html'] = html
            __props__['name'] = name
            __props__['subject'] = subject
            __props__['text'] = text
        super(Template, __self__).__init__(
            'aws:ses/template:Template',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            html: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            subject: Optional[pulumi.Input[str]] = None,
            text: Optional[pulumi.Input[str]] = None) -> 'Template':
        """
        Get an existing Template resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] html: The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        :param pulumi.Input[str] name: The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        :param pulumi.Input[str] subject: The subject line of the email.
        :param pulumi.Input[str] text: The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["html"] = html
        __props__["name"] = name
        __props__["subject"] = subject
        __props__["text"] = text
        return Template(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def html(self) -> pulumi.Output[Optional[str]]:
        """
        The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "html")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Output[Optional[str]]:
        """
        The subject line of the email.
        """
        return pulumi.get(self, "subject")

    @property
    @pulumi.getter
    def text(self) -> pulumi.Output[Optional[str]]:
        """
        The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "text")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

