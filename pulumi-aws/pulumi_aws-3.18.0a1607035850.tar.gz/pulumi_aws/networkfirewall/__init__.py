# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .firewall import *
from .firewall_policy import *
from .logging_configuration import *
from .resource_policy import *
from .rule_group import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:networkfirewall/firewall:Firewall":
                return Firewall(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:networkfirewall/firewallPolicy:FirewallPolicy":
                return FirewallPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:networkfirewall/loggingConfiguration:LoggingConfiguration":
                return LoggingConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:networkfirewall/resourcePolicy:ResourcePolicy":
                return ResourcePolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:networkfirewall/ruleGroup:RuleGroup":
                return RuleGroup(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "networkfirewall/firewall", _module_instance)
    pulumi.runtime.register_resource_module("aws", "networkfirewall/firewallPolicy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "networkfirewall/loggingConfiguration", _module_instance)
    pulumi.runtime.register_resource_module("aws", "networkfirewall/resourcePolicy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "networkfirewall/ruleGroup", _module_instance)

_register_module()
