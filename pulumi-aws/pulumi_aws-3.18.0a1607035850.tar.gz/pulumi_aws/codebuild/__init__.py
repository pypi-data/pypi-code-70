# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .project import *
from .report_group import *
from .source_credential import *
from .webhook import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:codebuild/project:Project":
                return Project(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:codebuild/reportGroup:ReportGroup":
                return ReportGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:codebuild/sourceCredential:SourceCredential":
                return SourceCredential(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:codebuild/webhook:Webhook":
                return Webhook(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "codebuild/project", _module_instance)
    pulumi.runtime.register_resource_module("aws", "codebuild/reportGroup", _module_instance)
    pulumi.runtime.register_resource_module("aws", "codebuild/sourceCredential", _module_instance)
    pulumi.runtime.register_resource_module("aws", "codebuild/webhook", _module_instance)

_register_module()
