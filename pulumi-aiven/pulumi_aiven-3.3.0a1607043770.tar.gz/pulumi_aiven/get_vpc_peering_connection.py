# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetVpcPeeringConnectionResult',
    'AwaitableGetVpcPeeringConnectionResult',
    'get_vpc_peering_connection',
]

@pulumi.output_type
class GetVpcPeeringConnectionResult:
    """
    A collection of values returned by getVpcPeeringConnection.
    """
    def __init__(__self__, id=None, peer_azure_app_id=None, peer_azure_tenant_id=None, peer_cloud_account=None, peer_region=None, peer_resource_group=None, peer_vpc=None, peering_connection_id=None, state=None, state_info=None, vpc_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if peer_azure_app_id and not isinstance(peer_azure_app_id, str):
            raise TypeError("Expected argument 'peer_azure_app_id' to be a str")
        pulumi.set(__self__, "peer_azure_app_id", peer_azure_app_id)
        if peer_azure_tenant_id and not isinstance(peer_azure_tenant_id, str):
            raise TypeError("Expected argument 'peer_azure_tenant_id' to be a str")
        pulumi.set(__self__, "peer_azure_tenant_id", peer_azure_tenant_id)
        if peer_cloud_account and not isinstance(peer_cloud_account, str):
            raise TypeError("Expected argument 'peer_cloud_account' to be a str")
        pulumi.set(__self__, "peer_cloud_account", peer_cloud_account)
        if peer_region and not isinstance(peer_region, str):
            raise TypeError("Expected argument 'peer_region' to be a str")
        pulumi.set(__self__, "peer_region", peer_region)
        if peer_resource_group and not isinstance(peer_resource_group, str):
            raise TypeError("Expected argument 'peer_resource_group' to be a str")
        pulumi.set(__self__, "peer_resource_group", peer_resource_group)
        if peer_vpc and not isinstance(peer_vpc, str):
            raise TypeError("Expected argument 'peer_vpc' to be a str")
        pulumi.set(__self__, "peer_vpc", peer_vpc)
        if peering_connection_id and not isinstance(peering_connection_id, str):
            raise TypeError("Expected argument 'peering_connection_id' to be a str")
        pulumi.set(__self__, "peering_connection_id", peering_connection_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_info and not isinstance(state_info, dict):
            raise TypeError("Expected argument 'state_info' to be a dict")
        pulumi.set(__self__, "state_info", state_info)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="peerAzureAppId")
    def peer_azure_app_id(self) -> Optional[str]:
        """
        an Azure app registration id in UUID4 form that is allowed to create a peering to the peer vnet.
        """
        return pulumi.get(self, "peer_azure_app_id")

    @property
    @pulumi.getter(name="peerAzureTenantId")
    def peer_azure_tenant_id(self) -> Optional[str]:
        """
        an Azure tenant id in UUID4 form.
        """
        return pulumi.get(self, "peer_azure_tenant_id")

    @property
    @pulumi.getter(name="peerCloudAccount")
    def peer_cloud_account(self) -> str:
        return pulumi.get(self, "peer_cloud_account")

    @property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> Optional[str]:
        """
        defines the region of the remote VPC if it is not in the same region as Aiven VPC.
        """
        return pulumi.get(self, "peer_region")

    @property
    @pulumi.getter(name="peerResourceGroup")
    def peer_resource_group(self) -> Optional[str]:
        """
        an Azure resource group name of the peered VPC.
        """
        return pulumi.get(self, "peer_resource_group")

    @property
    @pulumi.getter(name="peerVpc")
    def peer_vpc(self) -> str:
        return pulumi.get(self, "peer_vpc")

    @property
    @pulumi.getter(name="peeringConnectionId")
    def peering_connection_id(self) -> str:
        """
        a cloud provider identifier for the peering connection if available.
        """
        return pulumi.get(self, "peering_connection_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        is the state of the peering connection. This property is computed by Aiven 
        therefore cannot be set, only read. Where state can be one of: `APPROVED`,
        `PENDING_PEER`, `ACTIVE`, `DELETED`, `DELETED_BY_PEER`, `REJECTED_BY_PEER` and
        `INVALID_SPECIFICATION`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateInfo")
    def state_info(self) -> Mapping[str, Any]:
        """
        state-specific help or error information.
        """
        return pulumi.get(self, "state_info")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")


class AwaitableGetVpcPeeringConnectionResult(GetVpcPeeringConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcPeeringConnectionResult(
            id=self.id,
            peer_azure_app_id=self.peer_azure_app_id,
            peer_azure_tenant_id=self.peer_azure_tenant_id,
            peer_cloud_account=self.peer_cloud_account,
            peer_region=self.peer_region,
            peer_resource_group=self.peer_resource_group,
            peer_vpc=self.peer_vpc,
            peering_connection_id=self.peering_connection_id,
            state=self.state,
            state_info=self.state_info,
            vpc_id=self.vpc_id)


def get_vpc_peering_connection(peer_azure_app_id: Optional[str] = None,
                               peer_azure_tenant_id: Optional[str] = None,
                               peer_cloud_account: Optional[str] = None,
                               peer_region: Optional[str] = None,
                               peer_resource_group: Optional[str] = None,
                               peer_vpc: Optional[str] = None,
                               peering_connection_id: Optional[str] = None,
                               state: Optional[str] = None,
                               state_info: Optional[Mapping[str, Any]] = None,
                               vpc_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcPeeringConnectionResult:
    """
    ## # VPC Peering Connection Data Source

    The VPC Peering Connection data source provides information about the existing Aiven
    VPC Peering Connection.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    mypeeringconnection = aiven.get_vpc_peering_connection(peer_cloud_account="<PEER_ACCOUNT_ID>",
        peer_vpc="<PEER_VPC_ID/NAME>",
        vpc_id=aiven_project_vpc["myvpc"]["id"])
    ```


    :param str peer_azure_app_id: an Azure app registration id in UUID4 form that is allowed to create a peering to the peer vnet.
    :param str peer_azure_tenant_id: an Azure tenant id in UUID4 form.
    :param str peer_cloud_account: defines the identifier of the cloud account the VPC is being
           peered with.
    :param str peer_region: defines the region of the remote VPC if it is not in the same region as Aiven VPC.
    :param str peer_resource_group: an Azure resource group name of the peered VPC.
    :param str peer_vpc: defines the identifier or name of the remote VPC.
    :param str peering_connection_id: a cloud provider identifier for the peering connection if available.
    :param str state: is the state of the peering connection. This property is computed by Aiven 
           therefore cannot be set, only read. Where state can be one of: `APPROVED`,
           `PENDING_PEER`, `ACTIVE`, `DELETED`, `DELETED_BY_PEER`, `REJECTED_BY_PEER` and
           `INVALID_SPECIFICATION`.
    :param Mapping[str, Any] state_info: state-specific help or error information.
    :param str vpc_id: is the Aiven VPC the peering connection is associated with.
    """
    __args__ = dict()
    __args__['peerAzureAppId'] = peer_azure_app_id
    __args__['peerAzureTenantId'] = peer_azure_tenant_id
    __args__['peerCloudAccount'] = peer_cloud_account
    __args__['peerRegion'] = peer_region
    __args__['peerResourceGroup'] = peer_resource_group
    __args__['peerVpc'] = peer_vpc
    __args__['peeringConnectionId'] = peering_connection_id
    __args__['state'] = state
    __args__['stateInfo'] = state_info
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aiven:index/getVpcPeeringConnection:getVpcPeeringConnection', __args__, opts=opts, typ=GetVpcPeeringConnectionResult).value

    return AwaitableGetVpcPeeringConnectionResult(
        id=__ret__.id,
        peer_azure_app_id=__ret__.peer_azure_app_id,
        peer_azure_tenant_id=__ret__.peer_azure_tenant_id,
        peer_cloud_account=__ret__.peer_cloud_account,
        peer_region=__ret__.peer_region,
        peer_resource_group=__ret__.peer_resource_group,
        peer_vpc=__ret__.peer_vpc,
        peering_connection_id=__ret__.peering_connection_id,
        state=__ret__.state,
        state_info=__ret__.state_info,
        vpc_id=__ret__.vpc_id)
