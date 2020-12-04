# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'OrganizationAccount',
    'OrganizationNonMasterAccount',
    'OrganizationRoot',
    'OrganizationRootPolicyType',
    'OrganizationalUnitAccount',
    'GetOrganizationAccountResult',
    'GetOrganizationNonMasterAccountResult',
    'GetOrganizationRootResult',
    'GetOrganizationRootPolicyTypeResult',
    'GetOrganizationalUnitsChildrenResult',
]

@pulumi.output_type
class OrganizationAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OrganizationNonMasterAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OrganizationRoot(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 policy_types: Optional[Sequence['outputs.OrganizationRootPolicyType']] = None):
        """
        :param str arn: ARN of the root
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param Sequence['OrganizationRootPolicyTypeArgs'] policy_types: List of policy types enabled for this root. All elements have these attributes:
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_types is not None:
            pulumi.set(__self__, "policy_types", policy_types)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Optional[Sequence['outputs.OrganizationRootPolicyType']]:
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
        return pulumi.get(self, "policy_types")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OrganizationRootPolicyType(dict):
    def __init__(__self__, *,
                 status: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str status: The status of the policy type as it relates to the associated root
        """
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OrganizationalUnitAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None):
        """
        :param str arn: ARN of the organizational unit
        :param str email: Email of the account
        :param str id: Identifier of the organization unit
        :param str name: The name for the organizational unit
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the organization unit
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name for the organizational unit
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetOrganizationAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationNonMasterAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationRootResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 id: str,
                 name: str,
                 policy_types: Sequence['outputs.GetOrganizationRootPolicyTypeResult']):
        """
        :param str arn: ARN of the root
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param Sequence['GetOrganizationRootPolicyTypeArgs'] policy_types: List of policy types enabled for this root. All elements have these attributes:
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "policy_types", policy_types)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Sequence['outputs.GetOrganizationRootPolicyTypeResult']:
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
        return pulumi.get(self, "policy_types")


@pulumi.output_type
class GetOrganizationRootPolicyTypeResult(dict):
    def __init__(__self__, *,
                 status: str,
                 type: str):
        """
        :param str status: The status of the policy type as it relates to the associated root
        """
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class GetOrganizationalUnitsChildrenResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 id: str,
                 name: str):
        """
        :param str arn: ARN of the organizational unit
        :param str id: Parent identifier of the organizational units.
        :param str name: Name of the organizational unit
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the organizational unit
        """
        return pulumi.get(self, "name")


