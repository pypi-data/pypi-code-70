# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .access_point import *
from .file_system import *
from .file_system_policy import *
from .get_access_point import *
from .get_access_points import *
from .get_file_system import *
from .get_mount_target import *
from .mount_target import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:efs/accessPoint:AccessPoint":
                return AccessPoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:efs/fileSystem:FileSystem":
                return FileSystem(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:efs/fileSystemPolicy:FileSystemPolicy":
                return FileSystemPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:efs/mountTarget:MountTarget":
                return MountTarget(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "efs/accessPoint", _module_instance)
    pulumi.runtime.register_resource_module("aws", "efs/fileSystem", _module_instance)
    pulumi.runtime.register_resource_module("aws", "efs/fileSystemPolicy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "efs/mountTarget", _module_instance)

_register_module()
