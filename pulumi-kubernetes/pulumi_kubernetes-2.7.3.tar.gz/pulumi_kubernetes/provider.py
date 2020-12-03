# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Provider']


class Provider(pulumi.ProviderResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 enable_dry_run: Optional[pulumi.Input[bool]] = None,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 render_yaml_to_directory: Optional[pulumi.Input[str]] = None,
                 suppress_deprecation_warnings: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The provider type for the kubernetes package.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: If present, the name of the kubeconfig cluster to use.
        :param pulumi.Input[str] context: If present, the name of the kubeconfig context to use.
        :param pulumi.Input[bool] enable_dry_run: BETA FEATURE - If present and set to true, enable server-side diff calculations.
               This feature is in developer preview, and is disabled by default.
               
               This config can be specified in the following ways, using this precedence:
               1. This `enableDryRun` parameter.
               2. The `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.
        :param pulumi.Input[str] kubeconfig: The contents of a kubeconfig file or the path to a kubeconfig file. If this is set, this config will be used instead of $KUBECONFIG.
        :param pulumi.Input[str] namespace: If present, the default namespace to use. This flag is ignored for cluster-scoped resources.
               
               A namespace can be specified in multiple places, and the precedence is as follows:
               1. `.metadata.namespace` set on the resource.
               2. This `namespace` parameter.
               3. `namespace` set for the active context in the kubeconfig.
        :param pulumi.Input[str] render_yaml_to_directory: BETA FEATURE - If present, render resource manifests to this directory. In this mode, resources will not
               be created on a Kubernetes cluster, but the rendered manifests will be kept in sync with changes
               to the Pulumi program. This feature is in developer preview, and is disabled by default.
               
               Note that some computed Outputs such as status fields will not be populated
               since the resources are not created on a Kubernetes cluster. These Output values will remain undefined,
               and may result in an error if they are referenced by other resources. Also note that any secret values
               used in these resources will be rendered in plaintext to the resulting YAML.
        :param pulumi.Input[bool] suppress_deprecation_warnings: If present and set to true, suppress apiVersion deprecation warnings from the CLI.
               
               This config can be specified in the following ways, using this precedence:
               1. This `suppressDeprecationWarnings` parameter.
               2. The `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.
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

            __props__['cluster'] = cluster
            __props__['context'] = context
            if enable_dry_run is None:
                enable_dry_run = _utilities.get_env_bool('PULUMI_K8S_ENABLE_DRY_RUN')
            __props__['enable_dry_run'] = pulumi.Output.from_input(enable_dry_run).apply(pulumi.runtime.to_json) if enable_dry_run is not None else None
            if kubeconfig is None:
                kubeconfig = _utilities.get_env('KUBECONFIG')
            __props__['kubeconfig'] = kubeconfig
            __props__['namespace'] = namespace
            __props__['render_yaml_to_directory'] = render_yaml_to_directory
            if suppress_deprecation_warnings is None:
                suppress_deprecation_warnings = _utilities.get_env_bool('PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS')
            __props__['suppress_deprecation_warnings'] = pulumi.Output.from_input(suppress_deprecation_warnings).apply(pulumi.runtime.to_json) if suppress_deprecation_warnings is not None else None
        super(Provider, __self__).__init__(
            'kubernetes',
            resource_name,
            __props__,
            opts)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

