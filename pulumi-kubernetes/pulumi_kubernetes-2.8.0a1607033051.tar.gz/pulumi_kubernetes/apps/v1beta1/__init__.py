# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .ControllerRevision import *
from .ControllerRevisionList import *
from .Deployment import *
from .DeploymentList import *
from .StatefulSet import *
from .StatefulSetList import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "kubernetes:apps/v1beta1:ControllerRevision":
                return ControllerRevision(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:apps/v1beta1:ControllerRevisionList":
                return ControllerRevisionList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:apps/v1beta1:Deployment":
                return Deployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:apps/v1beta1:DeploymentList":
                return DeploymentList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:apps/v1beta1:StatefulSet":
                return StatefulSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:apps/v1beta1:StatefulSetList":
                return StatefulSetList(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("kubernetes", "apps/v1beta1", _module_instance)

_register_module()
