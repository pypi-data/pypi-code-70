# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['InfluxDb']


class InfluxDb(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_name: Optional[pulumi.Input[str]] = None,
                 influxdb: Optional[pulumi.Input[pulumi.InputType['InfluxDbInfluxdbArgs']]] = None,
                 influxdb_user_config: Optional[pulumi.Input[pulumi.InputType['InfluxDbInfluxdbUserConfigArgs']]] = None,
                 maintenance_window_dow: Optional[pulumi.Input[str]] = None,
                 maintenance_window_time: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 project_vpc_id: Optional[pulumi.Input[str]] = None,
                 service_integrations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InfluxDbServiceIntegrationArgs']]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 termination_protection: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # InfluxDB Resource

        The InfluxDB resource allows the creation and management of an Aiven InfluxDB services.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        inf1 = aiven.InfluxDb("inf1",
            project=data["aiven_project"]["pr1"]["project"],
            cloud_name="google-europe-west1",
            plan="startup-4",
            service_name="my-inf1",
            maintenance_window_dow="monday",
            maintenance_window_time="10:00:00",
            influxdb_user_config=aiven.InfluxDbInfluxdbUserConfigArgs(
                public_access=aiven.InfluxDbInfluxdbUserConfigPublicAccessArgs(
                    influxdb="true",
                ),
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_name: defines where the cloud provider and region where the service is hosted
               in. This can be changed freely after service is created. Changing the value will trigger
               a potentially lenghty migration process for the service. Format is cloud provider name
               (`aws`, `azure`, `do` `google`, `upcloud`, etc.), dash, and the cloud provider
               specific region name. These are documented on each Cloud provider's own support articles,
               like [here for Google](https://cloud.google.com/compute/docs/regions-zones/) and
               [here for AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
        :param pulumi.Input[pulumi.InputType['InfluxDbInfluxdbArgs']] influxdb: influxdb.conf configuration values
        :param pulumi.Input[pulumi.InputType['InfluxDbInfluxdbUserConfigArgs']] influxdb_user_config: defines InfluxDB specific additional configuration options. The following 
               configuration options available:
        :param pulumi.Input[str] maintenance_window_dow: day of week when maintenance operations should be performed. 
               One monday, tuesday, wednesday, etc.
        :param pulumi.Input[str] maintenance_window_time: time of day when maintenance operations should be performed. 
               UTC time in HH:mm:ss format.
        :param pulumi.Input[str] plan: defines what kind of computing resources are allocated for the service. It can
               be changed after creation, though there are some restrictions when going to a smaller
               plan such as the new plan must have sufficient amount of disk space to store all current
               data and switching to a plan with fewer nodes might not be supported. The basic plan
               names are `hobbyist`, `startup-x`, `business-x` and `premium-x` where `x` is
               (roughly) the amount of memory on each node (also other attributes like number of CPUs
               and amount of disk space varies but naming is based on memory). The exact options can be
               seen from the Aiven web console's Create Service dialog.
        :param pulumi.Input[str] project: identifies the project the service belongs to. To set up proper dependency
               between the project and the service, refer to the project as shown in the above example.
               Project cannot be changed later without destroying and re-creating the service.
        :param pulumi.Input[str] project_vpc_id: optionally specifies the VPC the service should run in. If the value
               is not set the service is not run inside a VPC. When set, the value should be given as a
               reference as shown above to set up dependencies correctly and the VPC must be in the same
               cloud and region as the service itself. Project can be freely moved to and from VPC after
               creation but doing so triggers migration to new servers so the operation can take
               significant amount of time to complete if the service has a lot of data.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InfluxDbServiceIntegrationArgs']]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
        :param pulumi.Input[str] service_name: specifies the actual name of the service. The name cannot be changed
               later without destroying and re-creating the service so name should be picked based on
               intended service usage rather than current attributes.
        :param pulumi.Input[bool] termination_protection: prevents the service from being deleted. It is recommended to
               set this to `true` for all production services to prevent unintentional service
               deletions. This does not shield against deleting databases or topics but for services
               with backups much of the content can at least be restored from backup in case accidental
               deletion is done.
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

            __props__['cloud_name'] = cloud_name
            __props__['influxdb'] = influxdb
            __props__['influxdb_user_config'] = influxdb_user_config
            __props__['maintenance_window_dow'] = maintenance_window_dow
            __props__['maintenance_window_time'] = maintenance_window_time
            __props__['plan'] = plan
            if project is None:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['project_vpc_id'] = project_vpc_id
            __props__['service_integrations'] = service_integrations
            if service_name is None:
                raise TypeError("Missing required property 'service_name'")
            __props__['service_name'] = service_name
            __props__['termination_protection'] = termination_protection
            __props__['components'] = None
            __props__['service_host'] = None
            __props__['service_password'] = None
            __props__['service_port'] = None
            __props__['service_type'] = None
            __props__['service_uri'] = None
            __props__['service_username'] = None
            __props__['state'] = None
        super(InfluxDb, __self__).__init__(
            'aiven:index/influxDb:InfluxDb',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cloud_name: Optional[pulumi.Input[str]] = None,
            components: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InfluxDbComponentArgs']]]]] = None,
            influxdb: Optional[pulumi.Input[pulumi.InputType['InfluxDbInfluxdbArgs']]] = None,
            influxdb_user_config: Optional[pulumi.Input[pulumi.InputType['InfluxDbInfluxdbUserConfigArgs']]] = None,
            maintenance_window_dow: Optional[pulumi.Input[str]] = None,
            maintenance_window_time: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            project_vpc_id: Optional[pulumi.Input[str]] = None,
            service_host: Optional[pulumi.Input[str]] = None,
            service_integrations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InfluxDbServiceIntegrationArgs']]]]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            service_password: Optional[pulumi.Input[str]] = None,
            service_port: Optional[pulumi.Input[int]] = None,
            service_type: Optional[pulumi.Input[str]] = None,
            service_uri: Optional[pulumi.Input[str]] = None,
            service_username: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            termination_protection: Optional[pulumi.Input[bool]] = None) -> 'InfluxDb':
        """
        Get an existing InfluxDb resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_name: defines where the cloud provider and region where the service is hosted
               in. This can be changed freely after service is created. Changing the value will trigger
               a potentially lenghty migration process for the service. Format is cloud provider name
               (`aws`, `azure`, `do` `google`, `upcloud`, etc.), dash, and the cloud provider
               specific region name. These are documented on each Cloud provider's own support articles,
               like [here for Google](https://cloud.google.com/compute/docs/regions-zones/) and
               [here for AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InfluxDbComponentArgs']]]] components: Service component information objects
        :param pulumi.Input[pulumi.InputType['InfluxDbInfluxdbArgs']] influxdb: influxdb.conf configuration values
        :param pulumi.Input[pulumi.InputType['InfluxDbInfluxdbUserConfigArgs']] influxdb_user_config: defines InfluxDB specific additional configuration options. The following 
               configuration options available:
        :param pulumi.Input[str] maintenance_window_dow: day of week when maintenance operations should be performed. 
               One monday, tuesday, wednesday, etc.
        :param pulumi.Input[str] maintenance_window_time: time of day when maintenance operations should be performed. 
               UTC time in HH:mm:ss format.
        :param pulumi.Input[str] plan: defines what kind of computing resources are allocated for the service. It can
               be changed after creation, though there are some restrictions when going to a smaller
               plan such as the new plan must have sufficient amount of disk space to store all current
               data and switching to a plan with fewer nodes might not be supported. The basic plan
               names are `hobbyist`, `startup-x`, `business-x` and `premium-x` where `x` is
               (roughly) the amount of memory on each node (also other attributes like number of CPUs
               and amount of disk space varies but naming is based on memory). The exact options can be
               seen from the Aiven web console's Create Service dialog.
        :param pulumi.Input[str] project: identifies the project the service belongs to. To set up proper dependency
               between the project and the service, refer to the project as shown in the above example.
               Project cannot be changed later without destroying and re-creating the service.
        :param pulumi.Input[str] project_vpc_id: optionally specifies the VPC the service should run in. If the value
               is not set the service is not run inside a VPC. When set, the value should be given as a
               reference as shown above to set up dependencies correctly and the VPC must be in the same
               cloud and region as the service itself. Project can be freely moved to and from VPC after
               creation but doing so triggers migration to new servers so the operation can take
               significant amount of time to complete if the service has a lot of data.
        :param pulumi.Input[str] service_host: InfluxDB hostname.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InfluxDbServiceIntegrationArgs']]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
        :param pulumi.Input[str] service_name: specifies the actual name of the service. The name cannot be changed
               later without destroying and re-creating the service so name should be picked based on
               intended service usage rather than current attributes.
        :param pulumi.Input[str] service_password: Password used for connecting to the InfluxDB service, if applicable.
        :param pulumi.Input[int] service_port: InfluxDB port.
        :param pulumi.Input[str] service_type: Aiven internal service type code
        :param pulumi.Input[str] service_uri: URI for connecting to the InfluxDB service.
        :param pulumi.Input[str] service_username: Username used for connecting to the InfluxDB service, if applicable.
        :param pulumi.Input[str] state: Service state.
        :param pulumi.Input[bool] termination_protection: prevents the service from being deleted. It is recommended to
               set this to `true` for all production services to prevent unintentional service
               deletions. This does not shield against deleting databases or topics but for services
               with backups much of the content can at least be restored from backup in case accidental
               deletion is done.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cloud_name"] = cloud_name
        __props__["components"] = components
        __props__["influxdb"] = influxdb
        __props__["influxdb_user_config"] = influxdb_user_config
        __props__["maintenance_window_dow"] = maintenance_window_dow
        __props__["maintenance_window_time"] = maintenance_window_time
        __props__["plan"] = plan
        __props__["project"] = project
        __props__["project_vpc_id"] = project_vpc_id
        __props__["service_host"] = service_host
        __props__["service_integrations"] = service_integrations
        __props__["service_name"] = service_name
        __props__["service_password"] = service_password
        __props__["service_port"] = service_port
        __props__["service_type"] = service_type
        __props__["service_uri"] = service_uri
        __props__["service_username"] = service_username
        __props__["state"] = state
        __props__["termination_protection"] = termination_protection
        return InfluxDb(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudName")
    def cloud_name(self) -> pulumi.Output[Optional[str]]:
        """
        defines where the cloud provider and region where the service is hosted
        in. This can be changed freely after service is created. Changing the value will trigger
        a potentially lenghty migration process for the service. Format is cloud provider name
        (`aws`, `azure`, `do` `google`, `upcloud`, etc.), dash, and the cloud provider
        specific region name. These are documented on each Cloud provider's own support articles,
        like [here for Google](https://cloud.google.com/compute/docs/regions-zones/) and
        [here for AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
        """
        return pulumi.get(self, "cloud_name")

    @property
    @pulumi.getter
    def components(self) -> pulumi.Output[Sequence['outputs.InfluxDbComponent']]:
        """
        Service component information objects
        """
        return pulumi.get(self, "components")

    @property
    @pulumi.getter
    def influxdb(self) -> pulumi.Output['outputs.InfluxDbInfluxdb']:
        """
        influxdb.conf configuration values
        """
        return pulumi.get(self, "influxdb")

    @property
    @pulumi.getter(name="influxdbUserConfig")
    def influxdb_user_config(self) -> pulumi.Output[Optional['outputs.InfluxDbInfluxdbUserConfig']]:
        """
        defines InfluxDB specific additional configuration options. The following 
        configuration options available:
        """
        return pulumi.get(self, "influxdb_user_config")

    @property
    @pulumi.getter(name="maintenanceWindowDow")
    def maintenance_window_dow(self) -> pulumi.Output[Optional[str]]:
        """
        day of week when maintenance operations should be performed. 
        One monday, tuesday, wednesday, etc.
        """
        return pulumi.get(self, "maintenance_window_dow")

    @property
    @pulumi.getter(name="maintenanceWindowTime")
    def maintenance_window_time(self) -> pulumi.Output[Optional[str]]:
        """
        time of day when maintenance operations should be performed. 
        UTC time in HH:mm:ss format.
        """
        return pulumi.get(self, "maintenance_window_time")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[str]]:
        """
        defines what kind of computing resources are allocated for the service. It can
        be changed after creation, though there are some restrictions when going to a smaller
        plan such as the new plan must have sufficient amount of disk space to store all current
        data and switching to a plan with fewer nodes might not be supported. The basic plan
        names are `hobbyist`, `startup-x`, `business-x` and `premium-x` where `x` is
        (roughly) the amount of memory on each node (also other attributes like number of CPUs
        and amount of disk space varies but naming is based on memory). The exact options can be
        seen from the Aiven web console's Create Service dialog.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        identifies the project the service belongs to. To set up proper dependency
        between the project and the service, refer to the project as shown in the above example.
        Project cannot be changed later without destroying and re-creating the service.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="projectVpcId")
    def project_vpc_id(self) -> pulumi.Output[Optional[str]]:
        """
        optionally specifies the VPC the service should run in. If the value
        is not set the service is not run inside a VPC. When set, the value should be given as a
        reference as shown above to set up dependencies correctly and the VPC must be in the same
        cloud and region as the service itself. Project can be freely moved to and from VPC after
        creation but doing so triggers migration to new servers so the operation can take
        significant amount of time to complete if the service has a lot of data.
        """
        return pulumi.get(self, "project_vpc_id")

    @property
    @pulumi.getter(name="serviceHost")
    def service_host(self) -> pulumi.Output[str]:
        """
        InfluxDB hostname.
        """
        return pulumi.get(self, "service_host")

    @property
    @pulumi.getter(name="serviceIntegrations")
    def service_integrations(self) -> pulumi.Output[Optional[Sequence['outputs.InfluxDbServiceIntegration']]]:
        """
        Service integrations to specify when creating a service. Not applied after initial service creation
        """
        return pulumi.get(self, "service_integrations")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        specifies the actual name of the service. The name cannot be changed
        later without destroying and re-creating the service so name should be picked based on
        intended service usage rather than current attributes.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="servicePassword")
    def service_password(self) -> pulumi.Output[str]:
        """
        Password used for connecting to the InfluxDB service, if applicable.
        """
        return pulumi.get(self, "service_password")

    @property
    @pulumi.getter(name="servicePort")
    def service_port(self) -> pulumi.Output[int]:
        """
        InfluxDB port.
        """
        return pulumi.get(self, "service_port")

    @property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Output[str]:
        """
        Aiven internal service type code
        """
        return pulumi.get(self, "service_type")

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> pulumi.Output[str]:
        """
        URI for connecting to the InfluxDB service.
        """
        return pulumi.get(self, "service_uri")

    @property
    @pulumi.getter(name="serviceUsername")
    def service_username(self) -> pulumi.Output[str]:
        """
        Username used for connecting to the InfluxDB service, if applicable.
        """
        return pulumi.get(self, "service_username")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Service state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        prevents the service from being deleted. It is recommended to
        set this to `true` for all production services to prevent unintentional service
        deletions. This does not shield against deleting databases or topics but for services
        with backups much of the content can at least be restored from backup in case accidental
        deletion is done.
        """
        return pulumi.get(self, "termination_protection")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

