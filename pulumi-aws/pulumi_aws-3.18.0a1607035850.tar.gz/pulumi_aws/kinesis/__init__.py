# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .analytics_application import *
from .firehose_delivery_stream import *
from .get_stream import *
from .stream import *
from .video_stream import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return None

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:kinesis/analyticsApplication:AnalyticsApplication":
                return AnalyticsApplication(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:kinesis/firehoseDeliveryStream:FirehoseDeliveryStream":
                return FirehoseDeliveryStream(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:kinesis/stream:Stream":
                return Stream(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:kinesis/videoStream:VideoStream":
                return VideoStream(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "kinesis/analyticsApplication", _module_instance)
    pulumi.runtime.register_resource_module("aws", "kinesis/firehoseDeliveryStream", _module_instance)
    pulumi.runtime.register_resource_module("aws", "kinesis/stream", _module_instance)
    pulumi.runtime.register_resource_module("aws", "kinesis/videoStream", _module_instance)

_register_module()
