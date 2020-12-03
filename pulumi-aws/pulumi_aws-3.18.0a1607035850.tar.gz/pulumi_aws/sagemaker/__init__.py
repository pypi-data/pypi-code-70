# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .code_repository import *
from .endpoint import *
from .endpoint_configuration import *
from .get_prebuilt_ecr_image import *
from .model import *
from .notebook_instance import *
from .notebook_instance_lifecycle_configuration import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:sagemaker/codeRepository:CodeRepository":
                return CodeRepository(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/endpoint:Endpoint":
                return Endpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/endpointConfiguration:EndpointConfiguration":
                return EndpointConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/model:Model":
                return Model(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/notebookInstance:NotebookInstance":
                return NotebookInstance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/notebookInstanceLifecycleConfiguration:NotebookInstanceLifecycleConfiguration":
                return NotebookInstanceLifecycleConfiguration(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "sagemaker/codeRepository", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/endpoint", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/endpointConfiguration", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/model", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/notebookInstance", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/notebookInstanceLifecycleConfiguration", _module_instance)

_register_module()
