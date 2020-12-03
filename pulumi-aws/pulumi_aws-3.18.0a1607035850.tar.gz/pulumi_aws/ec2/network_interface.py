# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['NetworkInterface']


class NetworkInterface(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceAttachmentArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ipv6_address_count: Optional[pulumi.Input[int]] = None,
                 ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_ip: Optional[pulumi.Input[str]] = None,
                 private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_ips_count: Optional[pulumi.Input[int]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_dest_check: Optional[pulumi.Input[bool]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Elastic network interface (ENI) resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.ec2.NetworkInterface("test",
            subnet_id=aws_subnet["public_a"]["id"],
            private_ips=["10.0.0.50"],
            security_groups=[aws_security_group["web"]["id"]],
            attachments=[aws.ec2.NetworkInterfaceAttachmentArgs(
                instance=aws_instance["test"]["id"],
                device_index=1,
            )])
        ```

        ## Import

        Network Interfaces can be imported using the `id`, e.g.

        ```sh
         $ pulumi import aws:ec2/networkInterface:NetworkInterface test eni-e5aa89a3
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceAttachmentArgs']]]] attachments: Block to define the attachment of the ENI. Documented below.
        :param pulumi.Input[str] description: A description for the network interface.
        :param pulumi.Input[int] ipv6_address_count: The number of IPv6 addresses to assign to a network interface. You can't use this option if specifying specific `ipv6_addresses`. If your subnet has the AssignIpv6AddressOnCreation attribute set to `true`, you can specify `0` to override this setting.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ipv6_addresses: One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you're specifying `ipv6_address_count`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_ips: List of private IPs to assign to the ENI.
        :param pulumi.Input[int] private_ips_count: Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: List of security group IDs to assign to the ENI.
        :param pulumi.Input[bool] source_dest_check: Whether to enable source destination checking for the ENI. Default true.
        :param pulumi.Input[str] subnet_id: Subnet ID to create the ENI in.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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

            __props__['attachments'] = attachments
            __props__['description'] = description
            __props__['ipv6_address_count'] = ipv6_address_count
            __props__['ipv6_addresses'] = ipv6_addresses
            __props__['private_ip'] = private_ip
            __props__['private_ips'] = private_ips
            __props__['private_ips_count'] = private_ips_count
            __props__['security_groups'] = security_groups
            __props__['source_dest_check'] = source_dest_check
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__['subnet_id'] = subnet_id
            __props__['tags'] = tags
            __props__['mac_address'] = None
            __props__['outpost_arn'] = None
            __props__['private_dns_name'] = None
        super(NetworkInterface, __self__).__init__(
            'aws:ec2/networkInterface:NetworkInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attachments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceAttachmentArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ipv6_address_count: Optional[pulumi.Input[int]] = None,
            ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            mac_address: Optional[pulumi.Input[str]] = None,
            outpost_arn: Optional[pulumi.Input[str]] = None,
            private_dns_name: Optional[pulumi.Input[str]] = None,
            private_ip: Optional[pulumi.Input[str]] = None,
            private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            private_ips_count: Optional[pulumi.Input[int]] = None,
            security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            source_dest_check: Optional[pulumi.Input[bool]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'NetworkInterface':
        """
        Get an existing NetworkInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceAttachmentArgs']]]] attachments: Block to define the attachment of the ENI. Documented below.
        :param pulumi.Input[str] description: A description for the network interface.
        :param pulumi.Input[int] ipv6_address_count: The number of IPv6 addresses to assign to a network interface. You can't use this option if specifying specific `ipv6_addresses`. If your subnet has the AssignIpv6AddressOnCreation attribute set to `true`, you can specify `0` to override this setting.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ipv6_addresses: One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you're specifying `ipv6_address_count`.
        :param pulumi.Input[str] mac_address: The MAC address of the network interface.
        :param pulumi.Input[str] private_dns_name: The private DNS name of the network interface (IPv4).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_ips: List of private IPs to assign to the ENI.
        :param pulumi.Input[int] private_ips_count: Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: List of security group IDs to assign to the ENI.
        :param pulumi.Input[bool] source_dest_check: Whether to enable source destination checking for the ENI. Default true.
        :param pulumi.Input[str] subnet_id: Subnet ID to create the ENI in.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["attachments"] = attachments
        __props__["description"] = description
        __props__["ipv6_address_count"] = ipv6_address_count
        __props__["ipv6_addresses"] = ipv6_addresses
        __props__["mac_address"] = mac_address
        __props__["outpost_arn"] = outpost_arn
        __props__["private_dns_name"] = private_dns_name
        __props__["private_ip"] = private_ip
        __props__["private_ips"] = private_ips
        __props__["private_ips_count"] = private_ips_count
        __props__["security_groups"] = security_groups
        __props__["source_dest_check"] = source_dest_check
        __props__["subnet_id"] = subnet_id
        __props__["tags"] = tags
        return NetworkInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attachments(self) -> pulumi.Output[Sequence['outputs.NetworkInterfaceAttachment']]:
        """
        Block to define the attachment of the ENI. Documented below.
        """
        return pulumi.get(self, "attachments")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the network interface.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> pulumi.Output[int]:
        """
        The number of IPv6 addresses to assign to a network interface. You can't use this option if specifying specific `ipv6_addresses`. If your subnet has the AssignIpv6AddressOnCreation attribute set to `true`, you can specify `0` to override this setting.
        """
        return pulumi.get(self, "ipv6_address_count")

    @property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you're specifying `ipv6_address_count`.
        """
        return pulumi.get(self, "ipv6_addresses")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[str]:
        """
        The MAC address of the network interface.
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "outpost_arn")

    @property
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> pulumi.Output[str]:
        """
        The private DNS name of the network interface (IPv4).
        """
        return pulumi.get(self, "private_dns_name")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[str]:
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="privateIps")
    def private_ips(self) -> pulumi.Output[Sequence[str]]:
        """
        List of private IPs to assign to the ENI.
        """
        return pulumi.get(self, "private_ips")

    @property
    @pulumi.getter(name="privateIpsCount")
    def private_ips_count(self) -> pulumi.Output[int]:
        """
        Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
        """
        return pulumi.get(self, "private_ips_count")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Sequence[str]]:
        """
        List of security group IDs to assign to the ENI.
        """
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable source destination checking for the ENI. Default true.
        """
        return pulumi.get(self, "source_dest_check")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        Subnet ID to create the ENI in.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

