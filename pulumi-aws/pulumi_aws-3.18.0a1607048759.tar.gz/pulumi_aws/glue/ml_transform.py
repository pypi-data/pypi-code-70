# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['MLTransform']


class MLTransform(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 glue_version: Optional[pulumi.Input[str]] = None,
                 input_record_tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MLTransformInputRecordTableArgs']]]]] = None,
                 max_capacity: Optional[pulumi.Input[float]] = None,
                 max_retries: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 number_of_workers: Optional[pulumi.Input[int]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['MLTransformParametersArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 worker_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Glue ML Transform resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_catalog_database = aws.glue.CatalogDatabase("testCatalogDatabase", name="example")
        test_catalog_table = aws.glue.CatalogTable("testCatalogTable",
            name="example",
            database_name=test_catalog_database.name,
            owner="my_owner",
            retention=1,
            table_type="VIRTUAL_VIEW",
            view_expanded_text="view_expanded_text_1",
            view_original_text="view_original_text_1",
            storage_descriptor=aws.glue.CatalogTableStorageDescriptorArgs(
                bucket_columns=["bucket_column_1"],
                compressed=False,
                input_format="SequenceFileInputFormat",
                location="my_location",
                number_of_buckets=1,
                output_format="SequenceFileInputFormat",
                stored_as_sub_directories=False,
                parameters={
                    "param1": "param1_val",
                },
                columns=[
                    aws.glue.CatalogTableStorageDescriptorColumnArgs(
                        name="my_column_1",
                        type="int",
                        comment="my_column1_comment",
                    ),
                    aws.glue.CatalogTableStorageDescriptorColumnArgs(
                        name="my_column_2",
                        type="string",
                        comment="my_column2_comment",
                    ),
                ],
                ser_de_info=aws.glue.CatalogTableStorageDescriptorSerDeInfoArgs(
                    name="ser_de_name",
                    parameters={
                        "param1": "param_val_1",
                    },
                    serialization_library="org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe",
                ),
                sort_columns=[aws.glue.CatalogTableStorageDescriptorSortColumnArgs(
                    column="my_column_1",
                    sort_order=1,
                )],
                skewed_info=aws.glue.CatalogTableStorageDescriptorSkewedInfoArgs(
                    skewed_column_names=["my_column_1"],
                    skewed_column_value_location_maps={
                        "my_column_1": "my_column_1_val_loc_map",
                    },
                    skewed_column_values=["skewed_val_1"],
                ),
            ),
            partition_keys=[
                aws.glue.CatalogTablePartitionKeyArgs(
                    name="my_column_1",
                    type="int",
                    comment="my_column_1_comment",
                ),
                aws.glue.CatalogTablePartitionKeyArgs(
                    name="my_column_2",
                    type="string",
                    comment="my_column_2_comment",
                ),
            ],
            parameters={
                "param1": "param1_val",
            })
        test_ml_transform = aws.glue.MLTransform("testMLTransform",
            role_arn=aws_iam_role["test"]["arn"],
            input_record_tables=[aws.glue.MLTransformInputRecordTableArgs(
                database_name=test_catalog_table.database_name,
                table_name=test_catalog_table.name,
            )],
            parameters=aws.glue.MLTransformParametersArgs(
                transform_type="FIND_MATCHES",
                find_matches_parameters=aws.glue.MLTransformParametersFindMatchesParametersArgs(
                    primary_key_column_name="my_column_1",
                ),
            ),
            opts=pulumi.ResourceOptions(depends_on=[aws_iam_role_policy_attachment["test"]]))
        ```

        ## Import

        Glue ML Transforms can be imported using `id`, e.g.

        ```sh
         $ pulumi import aws:glue/mLTransform:MLTransform example tfm-c2cafbe83b1c575f49eaca9939220e2fcd58e2d5
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the ML Transform.
        :param pulumi.Input[str] glue_version: The version of glue to use, for example "1.0". For information about available versions, see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MLTransformInputRecordTableArgs']]]] input_record_tables: A list of AWS Glue table definitions used by the transform. see Input Record Tables.
        :param pulumi.Input[float] max_capacity: The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from `2` to `100` DPUs; the default is `10`. `max_capacity` is a mutually exclusive option with `number_of_workers` and `worker_type`.
        :param pulumi.Input[int] max_retries: The maximum number of times to retry this ML Transform if it fails.
        :param pulumi.Input[str] name: The name you assign to this ML Transform. It must be unique in your account.
        :param pulumi.Input[int] number_of_workers: The number of workers of a defined `worker_type` that are allocated when an ML Transform runs. Required with `worker_type`.
        :param pulumi.Input[pulumi.InputType['MLTransformParametersArgs']] parameters: The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type. see Parameters.
        :param pulumi.Input[str] role_arn: The ARN of the IAM role associated with this ML Transform.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[int] timeout: The ML Transform timeout in minutes. The default is 2880 minutes (48 hours).
        :param pulumi.Input[str] worker_type: The type of predefined worker that is allocated when an ML Transform runs. Accepts a value of `Standard`, `G.1X`, or `G.2X`. Required with `number_of_workers`.
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

            __props__['description'] = description
            __props__['glue_version'] = glue_version
            if input_record_tables is None and not opts.urn:
                raise TypeError("Missing required property 'input_record_tables'")
            __props__['input_record_tables'] = input_record_tables
            __props__['max_capacity'] = max_capacity
            __props__['max_retries'] = max_retries
            __props__['name'] = name
            __props__['number_of_workers'] = number_of_workers
            if parameters is None and not opts.urn:
                raise TypeError("Missing required property 'parameters'")
            __props__['parameters'] = parameters
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['tags'] = tags
            __props__['timeout'] = timeout
            __props__['worker_type'] = worker_type
            __props__['arn'] = None
            __props__['label_count'] = None
            __props__['schemas'] = None
        super(MLTransform, __self__).__init__(
            'aws:glue/mLTransform:MLTransform',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            glue_version: Optional[pulumi.Input[str]] = None,
            input_record_tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MLTransformInputRecordTableArgs']]]]] = None,
            label_count: Optional[pulumi.Input[int]] = None,
            max_capacity: Optional[pulumi.Input[float]] = None,
            max_retries: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            number_of_workers: Optional[pulumi.Input[int]] = None,
            parameters: Optional[pulumi.Input[pulumi.InputType['MLTransformParametersArgs']]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            schemas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MLTransformSchemaArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timeout: Optional[pulumi.Input[int]] = None,
            worker_type: Optional[pulumi.Input[str]] = None) -> 'MLTransform':
        """
        Get an existing MLTransform resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Glue ML Transform.
        :param pulumi.Input[str] description: Description of the ML Transform.
        :param pulumi.Input[str] glue_version: The version of glue to use, for example "1.0". For information about available versions, see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MLTransformInputRecordTableArgs']]]] input_record_tables: A list of AWS Glue table definitions used by the transform. see Input Record Tables.
        :param pulumi.Input[int] label_count: The number of labels available for this transform.
        :param pulumi.Input[float] max_capacity: The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from `2` to `100` DPUs; the default is `10`. `max_capacity` is a mutually exclusive option with `number_of_workers` and `worker_type`.
        :param pulumi.Input[int] max_retries: The maximum number of times to retry this ML Transform if it fails.
        :param pulumi.Input[str] name: The name you assign to this ML Transform. It must be unique in your account.
        :param pulumi.Input[int] number_of_workers: The number of workers of a defined `worker_type` that are allocated when an ML Transform runs. Required with `worker_type`.
        :param pulumi.Input[pulumi.InputType['MLTransformParametersArgs']] parameters: The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type. see Parameters.
        :param pulumi.Input[str] role_arn: The ARN of the IAM role associated with this ML Transform.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MLTransformSchemaArgs']]]] schemas: The object that represents the schema that this transform accepts. see Schema.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[int] timeout: The ML Transform timeout in minutes. The default is 2880 minutes (48 hours).
        :param pulumi.Input[str] worker_type: The type of predefined worker that is allocated when an ML Transform runs. Accepts a value of `Standard`, `G.1X`, or `G.2X`. Required with `number_of_workers`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["glue_version"] = glue_version
        __props__["input_record_tables"] = input_record_tables
        __props__["label_count"] = label_count
        __props__["max_capacity"] = max_capacity
        __props__["max_retries"] = max_retries
        __props__["name"] = name
        __props__["number_of_workers"] = number_of_workers
        __props__["parameters"] = parameters
        __props__["role_arn"] = role_arn
        __props__["schemas"] = schemas
        __props__["tags"] = tags
        __props__["timeout"] = timeout
        __props__["worker_type"] = worker_type
        return MLTransform(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of Glue ML Transform.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the ML Transform.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> pulumi.Output[str]:
        """
        The version of glue to use, for example "1.0". For information about available versions, see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
        """
        return pulumi.get(self, "glue_version")

    @property
    @pulumi.getter(name="inputRecordTables")
    def input_record_tables(self) -> pulumi.Output[Sequence['outputs.MLTransformInputRecordTable']]:
        """
        A list of AWS Glue table definitions used by the transform. see Input Record Tables.
        """
        return pulumi.get(self, "input_record_tables")

    @property
    @pulumi.getter(name="labelCount")
    def label_count(self) -> pulumi.Output[int]:
        """
        The number of labels available for this transform.
        """
        return pulumi.get(self, "label_count")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Output[float]:
        """
        The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from `2` to `100` DPUs; the default is `10`. `max_capacity` is a mutually exclusive option with `number_of_workers` and `worker_type`.
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum number of times to retry this ML Transform if it fails.
        """
        return pulumi.get(self, "max_retries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name you assign to this ML Transform. It must be unique in your account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> pulumi.Output[Optional[int]]:
        """
        The number of workers of a defined `worker_type` that are allocated when an ML Transform runs. Required with `worker_type`.
        """
        return pulumi.get(self, "number_of_workers")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output['outputs.MLTransformParameters']:
        """
        The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type. see Parameters.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the IAM role associated with this ML Transform.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def schemas(self) -> pulumi.Output[Sequence['outputs.MLTransformSchema']]:
        """
        The object that represents the schema that this transform accepts. see Schema.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[int]]:
        """
        The ML Transform timeout in minutes. The default is 2880 minutes (48 hours).
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of predefined worker that is allocated when an ML Transform runs. Accepts a value of `Standard`, `G.1X`, or `G.2X`. Required with `number_of_workers`.
        """
        return pulumi.get(self, "worker_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

