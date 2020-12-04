# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'WindowsFileSystemSelfManagedActiveDirectoryArgs',
]

@pulumi.input_type
class WindowsFileSystemSelfManagedActiveDirectoryArgs:
    def __init__(__self__, *,
                 dns_ips: pulumi.Input[Sequence[pulumi.Input[str]]],
                 domain_name: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str],
                 file_system_administrators_group: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_ips: A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
        :param pulumi.Input[str] domain_name: The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
        :param pulumi.Input[str] password: The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        :param pulumi.Input[str] username: The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        :param pulumi.Input[str] file_system_administrators_group: The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
        :param pulumi.Input[str] organizational_unit_distinguished_name: The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
        """
        pulumi.set(__self__, "dns_ips", dns_ips)
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)
        if file_system_administrators_group is not None:
            pulumi.set(__self__, "file_system_administrators_group", file_system_administrators_group)
        if organizational_unit_distinguished_name is not None:
            pulumi.set(__self__, "organizational_unit_distinguished_name", organizational_unit_distinguished_name)

    @property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
        """
        return pulumi.get(self, "dns_ips")

    @dns_ips.setter
    def dns_ips(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "dns_ips", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
        """
        return pulumi.get(self, "file_system_administrators_group")

    @file_system_administrators_group.setter
    def file_system_administrators_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_system_administrators_group", value)

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
        """
        return pulumi.get(self, "organizational_unit_distinguished_name")

    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organizational_unit_distinguished_name", value)


