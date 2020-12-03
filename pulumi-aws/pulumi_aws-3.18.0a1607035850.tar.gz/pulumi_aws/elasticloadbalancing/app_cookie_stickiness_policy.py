# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['AppCookieStickinessPolicy']

warnings.warn("""aws.elasticloadbalancing.AppCookieStickinessPolicy has been deprecated in favor of aws.elb.AppCookieStickinessPolicy""", DeprecationWarning)


class AppCookieStickinessPolicy(pulumi.CustomResource):
    warnings.warn("""aws.elasticloadbalancing.AppCookieStickinessPolicy has been deprecated in favor of aws.elb.AppCookieStickinessPolicy""", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cookie_name: Optional[pulumi.Input[str]] = None,
                 lb_port: Optional[pulumi.Input[int]] = None,
                 load_balancer: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an application cookie stickiness policy, which allows an ELB to wed its sticky cookie's expiration to a cookie generated by your application.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        lb = aws.elb.LoadBalancer("lb",
            availability_zones=["us-east-1a"],
            listeners=[aws.elb.LoadBalancerListenerArgs(
                instance_port=8000,
                instance_protocol="http",
                lb_port=80,
                lb_protocol="http",
            )])
        foo = aws.elb.AppCookieStickinessPolicy("foo",
            load_balancer=lb.name,
            lb_port=80,
            cookie_name="MyAppCookie")
        ```

        ## Import

        Application cookie stickiness policies can be imported using the ELB name, port, and policy name separated by colons (`:`), e.g.

        ```sh
         $ pulumi import aws:elasticloadbalancing/appCookieStickinessPolicy:AppCookieStickinessPolicy example my-elb:80:my-policy
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cookie_name: The application cookie whose lifetime the ELB's cookie should follow.
        :param pulumi.Input[int] lb_port: The load balancer port to which the policy
               should be applied. This must be an active listener on the load
               balancer.
        :param pulumi.Input[str] load_balancer: The name of load balancer to which the policy
               should be attached.
        :param pulumi.Input[str] name: The name of the stickiness policy.
        """
        pulumi.log.warn("AppCookieStickinessPolicy is deprecated: aws.elasticloadbalancing.AppCookieStickinessPolicy has been deprecated in favor of aws.elb.AppCookieStickinessPolicy")
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

            if cookie_name is None and not opts.urn:
                raise TypeError("Missing required property 'cookie_name'")
            __props__['cookie_name'] = cookie_name
            if lb_port is None and not opts.urn:
                raise TypeError("Missing required property 'lb_port'")
            __props__['lb_port'] = lb_port
            if load_balancer is None and not opts.urn:
                raise TypeError("Missing required property 'load_balancer'")
            __props__['load_balancer'] = load_balancer
            __props__['name'] = name
        super(AppCookieStickinessPolicy, __self__).__init__(
            'aws:elasticloadbalancing/appCookieStickinessPolicy:AppCookieStickinessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cookie_name: Optional[pulumi.Input[str]] = None,
            lb_port: Optional[pulumi.Input[int]] = None,
            load_balancer: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'AppCookieStickinessPolicy':
        """
        Get an existing AppCookieStickinessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cookie_name: The application cookie whose lifetime the ELB's cookie should follow.
        :param pulumi.Input[int] lb_port: The load balancer port to which the policy
               should be applied. This must be an active listener on the load
               balancer.
        :param pulumi.Input[str] load_balancer: The name of load balancer to which the policy
               should be attached.
        :param pulumi.Input[str] name: The name of the stickiness policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cookie_name"] = cookie_name
        __props__["lb_port"] = lb_port
        __props__["load_balancer"] = load_balancer
        __props__["name"] = name
        return AppCookieStickinessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cookieName")
    def cookie_name(self) -> pulumi.Output[str]:
        """
        The application cookie whose lifetime the ELB's cookie should follow.
        """
        return pulumi.get(self, "cookie_name")

    @property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> pulumi.Output[int]:
        """
        The load balancer port to which the policy
        should be applied. This must be an active listener on the load
        balancer.
        """
        return pulumi.get(self, "lb_port")

    @property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[str]:
        """
        The name of load balancer to which the policy
        should be attached.
        """
        return pulumi.get(self, "load_balancer")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the stickiness policy.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

