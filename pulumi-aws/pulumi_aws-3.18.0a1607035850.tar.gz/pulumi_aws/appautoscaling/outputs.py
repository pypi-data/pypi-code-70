# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'PolicyStepScalingPolicyConfiguration',
    'PolicyStepScalingPolicyConfigurationStepAdjustment',
    'PolicyTargetTrackingScalingPolicyConfiguration',
    'PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification',
    'PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimension',
    'PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification',
    'ScheduledActionScalableTargetAction',
]

@pulumi.output_type
class PolicyStepScalingPolicyConfiguration(dict):
    def __init__(__self__, *,
                 adjustment_type: Optional[str] = None,
                 cooldown: Optional[int] = None,
                 metric_aggregation_type: Optional[str] = None,
                 min_adjustment_magnitude: Optional[int] = None,
                 step_adjustments: Optional[Sequence['outputs.PolicyStepScalingPolicyConfigurationStepAdjustment']] = None):
        """
        :param str adjustment_type: Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        :param int cooldown: The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        :param str metric_aggregation_type: The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        :param int min_adjustment_magnitude: The minimum number to adjust your scalable dimension as a result of a scaling activity. If the adjustment type is PercentChangeInCapacity, the scaling policy changes the scalable dimension of the scalable target by this amount.
        :param Sequence['PolicyStepScalingPolicyConfigurationStepAdjustmentArgs'] step_adjustments: A set of adjustments that manage scaling. These have the following structure:
        """
        if adjustment_type is not None:
            pulumi.set(__self__, "adjustment_type", adjustment_type)
        if cooldown is not None:
            pulumi.set(__self__, "cooldown", cooldown)
        if metric_aggregation_type is not None:
            pulumi.set(__self__, "metric_aggregation_type", metric_aggregation_type)
        if min_adjustment_magnitude is not None:
            pulumi.set(__self__, "min_adjustment_magnitude", min_adjustment_magnitude)
        if step_adjustments is not None:
            pulumi.set(__self__, "step_adjustments", step_adjustments)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[str]:
        """
        Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        """
        return pulumi.get(self, "adjustment_type")

    @property
    @pulumi.getter
    def cooldown(self) -> Optional[int]:
        """
        The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        """
        return pulumi.get(self, "cooldown")

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[str]:
        """
        The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        """
        return pulumi.get(self, "metric_aggregation_type")

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[int]:
        """
        The minimum number to adjust your scalable dimension as a result of a scaling activity. If the adjustment type is PercentChangeInCapacity, the scaling policy changes the scalable dimension of the scalable target by this amount.
        """
        return pulumi.get(self, "min_adjustment_magnitude")

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[Sequence['outputs.PolicyStepScalingPolicyConfigurationStepAdjustment']]:
        """
        A set of adjustments that manage scaling. These have the following structure:
        """
        return pulumi.get(self, "step_adjustments")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyStepScalingPolicyConfigurationStepAdjustment(dict):
    def __init__(__self__, *,
                 scaling_adjustment: int,
                 metric_interval_lower_bound: Optional[str] = None,
                 metric_interval_upper_bound: Optional[str] = None):
        """
        :param int scaling_adjustment: The number of members by which to scale, when the adjustment bounds are breached. A positive value scales up. A negative value scales down.
        :param str metric_interval_lower_bound: The lower bound for the difference between the alarm threshold and the CloudWatch metric. Without a value, AWS will treat this bound as negative infinity.
        :param str metric_interval_upper_bound: The upper bound for the difference between the alarm threshold and the CloudWatch metric. Without a value, AWS will treat this bound as infinity. The upper bound must be greater than the lower bound.
        """
        pulumi.set(__self__, "scaling_adjustment", scaling_adjustment)
        if metric_interval_lower_bound is not None:
            pulumi.set(__self__, "metric_interval_lower_bound", metric_interval_lower_bound)
        if metric_interval_upper_bound is not None:
            pulumi.set(__self__, "metric_interval_upper_bound", metric_interval_upper_bound)

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> int:
        """
        The number of members by which to scale, when the adjustment bounds are breached. A positive value scales up. A negative value scales down.
        """
        return pulumi.get(self, "scaling_adjustment")

    @property
    @pulumi.getter(name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> Optional[str]:
        """
        The lower bound for the difference between the alarm threshold and the CloudWatch metric. Without a value, AWS will treat this bound as negative infinity.
        """
        return pulumi.get(self, "metric_interval_lower_bound")

    @property
    @pulumi.getter(name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> Optional[str]:
        """
        The upper bound for the difference between the alarm threshold and the CloudWatch metric. Without a value, AWS will treat this bound as infinity. The upper bound must be greater than the lower bound.
        """
        return pulumi.get(self, "metric_interval_upper_bound")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfiguration(dict):
    def __init__(__self__, *,
                 target_value: float,
                 customized_metric_specification: Optional['outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification'] = None,
                 disable_scale_in: Optional[bool] = None,
                 predefined_metric_specification: Optional['outputs.PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification'] = None,
                 scale_in_cooldown: Optional[int] = None,
                 scale_out_cooldown: Optional[int] = None):
        """
        :param float target_value: The target value for the metric.
        :param 'PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs' customized_metric_specification: A custom CloudWatch metric. Documentation can be found  at: [AWS Customized Metric Specification](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CustomizedMetricSpecification.html). See supported fields below.
        :param bool disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is `false`.
        :param 'PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs' predefined_metric_specification: A predefined metric. See supported fields below.
        :param int scale_in_cooldown: The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.
        :param int scale_out_cooldown: The amount of time, in seconds, after a scale out activity completes before another scale out activity can start.
        """
        pulumi.set(__self__, "target_value", target_value)
        if customized_metric_specification is not None:
            pulumi.set(__self__, "customized_metric_specification", customized_metric_specification)
        if disable_scale_in is not None:
            pulumi.set(__self__, "disable_scale_in", disable_scale_in)
        if predefined_metric_specification is not None:
            pulumi.set(__self__, "predefined_metric_specification", predefined_metric_specification)
        if scale_in_cooldown is not None:
            pulumi.set(__self__, "scale_in_cooldown", scale_in_cooldown)
        if scale_out_cooldown is not None:
            pulumi.set(__self__, "scale_out_cooldown", scale_out_cooldown)

    @property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> float:
        """
        The target value for the metric.
        """
        return pulumi.get(self, "target_value")

    @property
    @pulumi.getter(name="customizedMetricSpecification")
    def customized_metric_specification(self) -> Optional['outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification']:
        """
        A custom CloudWatch metric. Documentation can be found  at: [AWS Customized Metric Specification](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CustomizedMetricSpecification.html). See supported fields below.
        """
        return pulumi.get(self, "customized_metric_specification")

    @property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[bool]:
        """
        Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is `false`.
        """
        return pulumi.get(self, "disable_scale_in")

    @property
    @pulumi.getter(name="predefinedMetricSpecification")
    def predefined_metric_specification(self) -> Optional['outputs.PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification']:
        """
        A predefined metric. See supported fields below.
        """
        return pulumi.get(self, "predefined_metric_specification")

    @property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[int]:
        """
        The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.
        """
        return pulumi.get(self, "scale_in_cooldown")

    @property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[int]:
        """
        The amount of time, in seconds, after a scale out activity completes before another scale out activity can start.
        """
        return pulumi.get(self, "scale_out_cooldown")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(dict):
    def __init__(__self__, *,
                 metric_name: str,
                 namespace: str,
                 statistic: str,
                 dimensions: Optional[Sequence['outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimension']] = None,
                 unit: Optional[str] = None):
        """
        :param str metric_name: The name of the metric.
        :param str namespace: The namespace of the metric.
        :param str statistic: The statistic of the metric. Valid values: `Average`, `Minimum`, `Maximum`, `SampleCount`, and `Sum`.
        :param Sequence['PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionArgs'] dimensions: Configuration block(s) with the dimensions of the metric if the metric was published with dimensions. Detailed below.
        :param str unit: The unit of the metric.
        """
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "statistic", statistic)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> str:
        """
        The name of the metric.
        """
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        The namespace of the metric.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def statistic(self) -> str:
        """
        The statistic of the metric. Valid values: `Average`, `Minimum`, `Maximum`, `SampleCount`, and `Sum`.
        """
        return pulumi.get(self, "statistic")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimension']]:
        """
        Configuration block(s) with the dimensions of the metric if the metric was published with dimensions. Detailed below.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter
    def unit(self) -> Optional[str]:
        """
        The unit of the metric.
        """
        return pulumi.get(self, "unit")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimension(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        :param str name: The name of the policy. Must be between 1 and 255 characters in length.
        :param str value: Value of the dimension.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Value of the dimension.
        """
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(dict):
    def __init__(__self__, *,
                 predefined_metric_type: str,
                 resource_label: Optional[str] = None):
        """
        :param str predefined_metric_type: The metric type.
        :param str resource_label: Reserved for future use. Must be less than or equal to 1023 characters in length.
        """
        pulumi.set(__self__, "predefined_metric_type", predefined_metric_type)
        if resource_label is not None:
            pulumi.set(__self__, "resource_label", resource_label)

    @property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> str:
        """
        The metric type.
        """
        return pulumi.get(self, "predefined_metric_type")

    @property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[str]:
        """
        Reserved for future use. Must be less than or equal to 1023 characters in length.
        """
        return pulumi.get(self, "resource_label")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ScheduledActionScalableTargetAction(dict):
    def __init__(__self__, *,
                 max_capacity: Optional[int] = None,
                 min_capacity: Optional[int] = None):
        """
        :param int max_capacity: The maximum capacity.
        :param int min_capacity: The minimum capacity.
        """
        if max_capacity is not None:
            pulumi.set(__self__, "max_capacity", max_capacity)
        if min_capacity is not None:
            pulumi.set(__self__, "min_capacity", min_capacity)

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[int]:
        """
        The maximum capacity.
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[int]:
        """
        The minimum capacity.
        """
        return pulumi.get(self, "min_capacity")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


