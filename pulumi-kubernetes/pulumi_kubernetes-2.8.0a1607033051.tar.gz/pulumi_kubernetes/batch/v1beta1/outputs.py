# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ... import batch as _batch
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'CronJob',
    'CronJobSpec',
    'CronJobStatus',
    'JobTemplateSpec',
]

@pulumi.output_type
class CronJob(dict):
    """
    CronJob represents the configuration of a single cron job.
    """
    def __init__(__self__, *,
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 spec: Optional['outputs.CronJobSpec'] = None,
                 status: Optional['outputs.CronJobStatus'] = None):
        """
        CronJob represents the configuration of a single cron job.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param 'CronJobSpecArgs' spec: Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        :param 'CronJobStatusArgs' status: Current status of a cron job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'batch/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'CronJob')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def spec(self) -> Optional['outputs.CronJobSpec']:
        """
        Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> Optional['outputs.CronJobStatus']:
        """
        Current status of a cron job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        return pulumi.get(self, "status")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CronJobSpec(dict):
    """
    CronJobSpec describes how the job execution will look like and when it will actually run.
    """
    def __init__(__self__, *,
                 job_template: 'outputs.JobTemplateSpec',
                 schedule: str,
                 concurrency_policy: Optional[str] = None,
                 failed_jobs_history_limit: Optional[int] = None,
                 starting_deadline_seconds: Optional[int] = None,
                 successful_jobs_history_limit: Optional[int] = None,
                 suspend: Optional[bool] = None):
        """
        CronJobSpec describes how the job execution will look like and when it will actually run.
        :param 'JobTemplateSpecArgs' job_template: Specifies the job that will be created when executing a CronJob.
        :param str schedule: The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.
        :param str concurrency_policy: Specifies how to treat concurrent executions of a Job. Valid values are: - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - "Replace": cancels currently running job and replaces it with a new one
        :param int failed_jobs_history_limit: The number of failed finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.
        :param int starting_deadline_seconds: Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.
        :param int successful_jobs_history_limit: The number of successful finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 3.
        :param bool suspend: This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.
        """
        pulumi.set(__self__, "job_template", job_template)
        pulumi.set(__self__, "schedule", schedule)
        if concurrency_policy is not None:
            pulumi.set(__self__, "concurrency_policy", concurrency_policy)
        if failed_jobs_history_limit is not None:
            pulumi.set(__self__, "failed_jobs_history_limit", failed_jobs_history_limit)
        if starting_deadline_seconds is not None:
            pulumi.set(__self__, "starting_deadline_seconds", starting_deadline_seconds)
        if successful_jobs_history_limit is not None:
            pulumi.set(__self__, "successful_jobs_history_limit", successful_jobs_history_limit)
        if suspend is not None:
            pulumi.set(__self__, "suspend", suspend)

    @property
    @pulumi.getter(name="jobTemplate")
    def job_template(self) -> 'outputs.JobTemplateSpec':
        """
        Specifies the job that will be created when executing a CronJob.
        """
        return pulumi.get(self, "job_template")

    @property
    @pulumi.getter
    def schedule(self) -> str:
        """
        The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="concurrencyPolicy")
    def concurrency_policy(self) -> Optional[str]:
        """
        Specifies how to treat concurrent executions of a Job. Valid values are: - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - "Replace": cancels currently running job and replaces it with a new one
        """
        return pulumi.get(self, "concurrency_policy")

    @property
    @pulumi.getter(name="failedJobsHistoryLimit")
    def failed_jobs_history_limit(self) -> Optional[int]:
        """
        The number of failed finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.
        """
        return pulumi.get(self, "failed_jobs_history_limit")

    @property
    @pulumi.getter(name="startingDeadlineSeconds")
    def starting_deadline_seconds(self) -> Optional[int]:
        """
        Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.
        """
        return pulumi.get(self, "starting_deadline_seconds")

    @property
    @pulumi.getter(name="successfulJobsHistoryLimit")
    def successful_jobs_history_limit(self) -> Optional[int]:
        """
        The number of successful finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 3.
        """
        return pulumi.get(self, "successful_jobs_history_limit")

    @property
    @pulumi.getter
    def suspend(self) -> Optional[bool]:
        """
        This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.
        """
        return pulumi.get(self, "suspend")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CronJobStatus(dict):
    """
    CronJobStatus represents the current state of a cron job.
    """
    def __init__(__self__, *,
                 active: Optional[Sequence['_core.v1.outputs.ObjectReference']] = None,
                 last_schedule_time: Optional[str] = None):
        """
        CronJobStatus represents the current state of a cron job.
        :param Sequence['_core.v1.ObjectReferenceArgs'] active: A list of pointers to currently running jobs.
        :param str last_schedule_time: Information when was the last time the job was successfully scheduled.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if last_schedule_time is not None:
            pulumi.set(__self__, "last_schedule_time", last_schedule_time)

    @property
    @pulumi.getter
    def active(self) -> Optional[Sequence['_core.v1.outputs.ObjectReference']]:
        """
        A list of pointers to currently running jobs.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="lastScheduleTime")
    def last_schedule_time(self) -> Optional[str]:
        """
        Information when was the last time the job was successfully scheduled.
        """
        return pulumi.get(self, "last_schedule_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class JobTemplateSpec(dict):
    """
    JobTemplateSpec describes the data a Job should have when created from a template
    """
    def __init__(__self__, *,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 spec: Optional['_batch.v1.outputs.JobSpec'] = None):
        """
        JobTemplateSpec describes the data a Job should have when created from a template
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param '_batch.v1.JobSpecArgs' spec: Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def spec(self) -> Optional['_batch.v1.outputs.JobSpec']:
        """
        Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        return pulumi.get(self, "spec")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


