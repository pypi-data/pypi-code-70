# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['ProjectVpc']


class ProjectVpc(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_name: Optional[pulumi.Input[str]] = None,
                 network_cidr: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # Project VPC Resource

        The Project VPC resource allows the creation and management of an Aiven Project VPCs.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        myvpc = aiven.ProjectVpc("myvpc",
            cloud_name="google-europe-west1",
            network_cidr="192.168.0.1/24",
            project=aiven_project["myproject"]["project"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_name: defines where the cloud provider and region where the service is hosted
               in. See the Service resource for additional information.
        :param pulumi.Input[str] network_cidr: defines the network CIDR of the VPC.
        :param pulumi.Input[str] project: defines the project the VPC belongs to.
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

            if cloud_name is None:
                raise TypeError("Missing required property 'cloud_name'")
            __props__['cloud_name'] = cloud_name
            if network_cidr is None:
                raise TypeError("Missing required property 'network_cidr'")
            __props__['network_cidr'] = network_cidr
            if project is None:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['state'] = None
        super(ProjectVpc, __self__).__init__(
            'aiven:index/projectVpc:ProjectVpc',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cloud_name: Optional[pulumi.Input[str]] = None,
            network_cidr: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'ProjectVpc':
        """
        Get an existing ProjectVpc resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_name: defines where the cloud provider and region where the service is hosted
               in. See the Service resource for additional information.
        :param pulumi.Input[str] network_cidr: defines the network CIDR of the VPC.
        :param pulumi.Input[str] project: defines the project the VPC belongs to.
        :param pulumi.Input[str] state: ia a computed property that tells the current state of the VPC. This property cannot be
               set, only read.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cloud_name"] = cloud_name
        __props__["network_cidr"] = network_cidr
        __props__["project"] = project
        __props__["state"] = state
        return ProjectVpc(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudName")
    def cloud_name(self) -> pulumi.Output[str]:
        """
        defines where the cloud provider and region where the service is hosted
        in. See the Service resource for additional information.
        """
        return pulumi.get(self, "cloud_name")

    @property
    @pulumi.getter(name="networkCidr")
    def network_cidr(self) -> pulumi.Output[str]:
        """
        defines the network CIDR of the VPC.
        """
        return pulumi.get(self, "network_cidr")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        defines the project the VPC belongs to.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        ia a computed property that tells the current state of the VPC. This property cannot be
        set, only read.
        """
        return pulumi.get(self, "state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

