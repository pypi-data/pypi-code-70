# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .certificate import *
from .get_endpoint import *
from .policy import *
from .policy_attachment import *
from .role_alias import *
from .thing import *
from .thing_principal_attachment import *
from .thing_type import *
from .topic_rule import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:iot/certificate:Certificate":
                return Certificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:iot/policy:Policy":
                return Policy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:iot/policyAttachment:PolicyAttachment":
                return PolicyAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:iot/roleAlias:RoleAlias":
                return RoleAlias(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:iot/thing:Thing":
                return Thing(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:iot/thingPrincipalAttachment:ThingPrincipalAttachment":
                return ThingPrincipalAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:iot/thingType:ThingType":
                return ThingType(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:iot/topicRule:TopicRule":
                return TopicRule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "iot/certificate", _module_instance)
    pulumi.runtime.register_resource_module("aws", "iot/policy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "iot/policyAttachment", _module_instance)
    pulumi.runtime.register_resource_module("aws", "iot/roleAlias", _module_instance)
    pulumi.runtime.register_resource_module("aws", "iot/thing", _module_instance)
    pulumi.runtime.register_resource_module("aws", "iot/thingPrincipalAttachment", _module_instance)
    pulumi.runtime.register_resource_module("aws", "iot/thingType", _module_instance)
    pulumi.runtime.register_resource_module("aws", "iot/topicRule", _module_instance)

_register_module()
