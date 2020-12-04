# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Queue']


class Queue(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_based_deduplication: Optional[pulumi.Input[bool]] = None,
                 delay_seconds: Optional[pulumi.Input[int]] = None,
                 fifo_queue: Optional[pulumi.Input[bool]] = None,
                 kms_data_key_reuse_period_seconds: Optional[pulumi.Input[int]] = None,
                 kms_master_key_id: Optional[pulumi.Input[str]] = None,
                 max_message_size: Optional[pulumi.Input[int]] = None,
                 message_retention_seconds: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 receive_wait_time_seconds: Optional[pulumi.Input[int]] = None,
                 redrive_policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 visibility_timeout_seconds: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        queue = aws.sqs.Queue("queue",
            delay_seconds=90,
            max_message_size=2048,
            message_retention_seconds=86400,
            receive_wait_time_seconds=10,
            redrive_policy=json.dumps({
                "deadLetterTargetArn": aws_sqs_queue["queue_deadletter"]["arn"],
                "maxReceiveCount": 4,
            }),
            tags={
                "Environment": "production",
            })
        ```
        ## FIFO queue

        ```python
        import pulumi
        import pulumi_aws as aws

        queue = aws.sqs.Queue("queue",
            content_based_deduplication=True,
            fifo_queue=True)
        ```

        ## Server-side encryption (SSE)

        ```python
        import pulumi
        import pulumi_aws as aws

        queue = aws.sqs.Queue("queue",
            kms_data_key_reuse_period_seconds=300,
            kms_master_key_id="alias/aws/sqs")
        ```

        ## Import

        SQS Queues can be imported using the `queue url`, e.g.

        ```sh
         $ pulumi import aws:sqs/queue:Queue public_queue https://queue.amazonaws.com/80398EXAMPLE/MyQueue
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] content_based_deduplication: Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)
        :param pulumi.Input[int] delay_seconds: The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.
        :param pulumi.Input[bool] fifo_queue: Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.
        :param pulumi.Input[int] kms_data_key_reuse_period_seconds: The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).
        :param pulumi.Input[str] kms_master_key_id: The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).
        :param pulumi.Input[int] max_message_size: The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
        :param pulumi.Input[int] message_retention_seconds: The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
        :param pulumi.Input[str] name: This is the human-readable name of the queue. If omitted, this provider will assign a random name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] policy: The JSON policy for the SQS queue.
        :param pulumi.Input[int] receive_wait_time_seconds: The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.
        :param pulumi.Input[str] redrive_policy: The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the queue.
        :param pulumi.Input[int] visibility_timeout_seconds: The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['content_based_deduplication'] = content_based_deduplication
            __props__['delay_seconds'] = delay_seconds
            __props__['fifo_queue'] = fifo_queue
            __props__['kms_data_key_reuse_period_seconds'] = kms_data_key_reuse_period_seconds
            __props__['kms_master_key_id'] = kms_master_key_id
            __props__['max_message_size'] = max_message_size
            __props__['message_retention_seconds'] = message_retention_seconds
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['policy'] = policy
            __props__['receive_wait_time_seconds'] = receive_wait_time_seconds
            __props__['redrive_policy'] = redrive_policy
            __props__['tags'] = tags
            __props__['visibility_timeout_seconds'] = visibility_timeout_seconds
            __props__['arn'] = None
        super(Queue, __self__).__init__(
            'aws:sqs/queue:Queue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            content_based_deduplication: Optional[pulumi.Input[bool]] = None,
            delay_seconds: Optional[pulumi.Input[int]] = None,
            fifo_queue: Optional[pulumi.Input[bool]] = None,
            kms_data_key_reuse_period_seconds: Optional[pulumi.Input[int]] = None,
            kms_master_key_id: Optional[pulumi.Input[str]] = None,
            max_message_size: Optional[pulumi.Input[int]] = None,
            message_retention_seconds: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            receive_wait_time_seconds: Optional[pulumi.Input[int]] = None,
            redrive_policy: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            visibility_timeout_seconds: Optional[pulumi.Input[int]] = None) -> 'Queue':
        """
        Get an existing Queue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the SQS queue
        :param pulumi.Input[bool] content_based_deduplication: Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)
        :param pulumi.Input[int] delay_seconds: The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.
        :param pulumi.Input[bool] fifo_queue: Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.
        :param pulumi.Input[int] kms_data_key_reuse_period_seconds: The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).
        :param pulumi.Input[str] kms_master_key_id: The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).
        :param pulumi.Input[int] max_message_size: The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
        :param pulumi.Input[int] message_retention_seconds: The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
        :param pulumi.Input[str] name: This is the human-readable name of the queue. If omitted, this provider will assign a random name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] policy: The JSON policy for the SQS queue.
        :param pulumi.Input[int] receive_wait_time_seconds: The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.
        :param pulumi.Input[str] redrive_policy: The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the queue.
        :param pulumi.Input[int] visibility_timeout_seconds: The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["content_based_deduplication"] = content_based_deduplication
        __props__["delay_seconds"] = delay_seconds
        __props__["fifo_queue"] = fifo_queue
        __props__["kms_data_key_reuse_period_seconds"] = kms_data_key_reuse_period_seconds
        __props__["kms_master_key_id"] = kms_master_key_id
        __props__["max_message_size"] = max_message_size
        __props__["message_retention_seconds"] = message_retention_seconds
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["policy"] = policy
        __props__["receive_wait_time_seconds"] = receive_wait_time_seconds
        __props__["redrive_policy"] = redrive_policy
        __props__["tags"] = tags
        __props__["visibility_timeout_seconds"] = visibility_timeout_seconds
        return Queue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the SQS queue
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)
        """
        return pulumi.get(self, "content_based_deduplication")

    @property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.
        """
        return pulumi.get(self, "delay_seconds")

    @property
    @pulumi.getter(name="fifoQueue")
    def fifo_queue(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.
        """
        return pulumi.get(self, "fifo_queue")

    @property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(self) -> pulumi.Output[int]:
        """
        The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).
        """
        return pulumi.get(self, "kms_data_key_reuse_period_seconds")

    @property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).
        """
        return pulumi.get(self, "kms_master_key_id")

    @property
    @pulumi.getter(name="maxMessageSize")
    def max_message_size(self) -> pulumi.Output[Optional[int]]:
        """
        The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
        """
        return pulumi.get(self, "max_message_size")

    @property
    @pulumi.getter(name="messageRetentionSeconds")
    def message_retention_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
        """
        return pulumi.get(self, "message_retention_seconds")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        This is the human-readable name of the queue. If omitted, this provider will assign a random name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        The JSON policy for the SQS queue.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="receiveWaitTimeSeconds")
    def receive_wait_time_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.
        """
        return pulumi.get(self, "receive_wait_time_seconds")

    @property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).
        """
        return pulumi.get(self, "redrive_policy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the queue.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="visibilityTimeoutSeconds")
    def visibility_timeout_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).
        """
        return pulumi.get(self, "visibility_timeout_seconds")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

