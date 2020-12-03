# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .encryption_config import *
from .group import *
from .sampling_rule import *

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:xray/encryptionConfig:EncryptionConfig":
                return EncryptionConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:xray/group:Group":
                return Group(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:xray/samplingRule:SamplingRule":
                return SamplingRule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "xray/encryptionConfig", _module_instance)
    pulumi.runtime.register_resource_module("aws", "xray/group", _module_instance)
    pulumi.runtime.register_resource_module("aws", "xray/samplingRule", _module_instance)

_register_module()
