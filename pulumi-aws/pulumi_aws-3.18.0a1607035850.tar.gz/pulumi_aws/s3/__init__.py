# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .access_point import *
from .account_public_access_block import *
from .analytics_configuration import *
from .bucket import *
from .bucket_metric import *
from .bucket_notification import *
from .bucket_object import *
from .bucket_ownership_controls import *
from .bucket_policy import *
from .bucket_public_access_block import *
from .get_bucket import *
from .get_bucket_object import *
from .get_bucket_objects import *
from .inventory import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:s3/accessPoint:AccessPoint":
                return AccessPoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/accountPublicAccessBlock:AccountPublicAccessBlock":
                return AccountPublicAccessBlock(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/analyticsConfiguration:AnalyticsConfiguration":
                return AnalyticsConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/bucket:Bucket":
                return Bucket(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/bucketMetric:BucketMetric":
                return BucketMetric(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/bucketNotification:BucketNotification":
                return BucketNotification(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/bucketObject:BucketObject":
                return BucketObject(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/bucketOwnershipControls:BucketOwnershipControls":
                return BucketOwnershipControls(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/bucketPolicy:BucketPolicy":
                return BucketPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/bucketPublicAccessBlock:BucketPublicAccessBlock":
                return BucketPublicAccessBlock(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:s3/inventory:Inventory":
                return Inventory(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "s3/accessPoint", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/accountPublicAccessBlock", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/analyticsConfiguration", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/bucket", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/bucketMetric", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/bucketNotification", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/bucketObject", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/bucketOwnershipControls", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/bucketPolicy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/bucketPublicAccessBlock", _module_instance)
    pulumi.runtime.register_resource_module("aws", "s3/inventory", _module_instance)

_register_module()
