# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'RepositoryEncryptionConfiguration',
    'RepositoryImageScanningConfiguration',
    'GetRepositoryEncryptionConfigurationResult',
    'GetRepositoryImageScanningConfigurationResult',
]

@pulumi.output_type
class RepositoryEncryptionConfiguration(dict):
    def __init__(__self__, *,
                 encryption_type: Optional[str] = None,
                 kms_key: Optional[str] = None):
        """
        :param str encryption_type: The encryption type to use for the repository. Valid values are `AES256` or `KMS`. Defaults to `AES256`.
        :param str kms_key: The ARN of the KMS key to use when `encryption_type` is `KMS`. If not specified, uses the default AWS managed key for ECR.
        """
        if encryption_type is not None:
            pulumi.set(__self__, "encryption_type", encryption_type)
        if kms_key is not None:
            pulumi.set(__self__, "kms_key", kms_key)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[str]:
        """
        The encryption type to use for the repository. Valid values are `AES256` or `KMS`. Defaults to `AES256`.
        """
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[str]:
        """
        The ARN of the KMS key to use when `encryption_type` is `KMS`. If not specified, uses the default AWS managed key for ECR.
        """
        return pulumi.get(self, "kms_key")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RepositoryImageScanningConfiguration(dict):
    def __init__(__self__, *,
                 scan_on_push: bool):
        """
        :param bool scan_on_push: Indicates whether images are scanned after being pushed to the repository (true) or not scanned (false).
        """
        pulumi.set(__self__, "scan_on_push", scan_on_push)

    @property
    @pulumi.getter(name="scanOnPush")
    def scan_on_push(self) -> bool:
        """
        Indicates whether images are scanned after being pushed to the repository (true) or not scanned (false).
        """
        return pulumi.get(self, "scan_on_push")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetRepositoryEncryptionConfigurationResult(dict):
    def __init__(__self__, *,
                 encryption_type: str,
                 kms_key: str):
        """
        :param str encryption_type: The encryption type to use for the repository, either `AES256` or `KMS`.
        :param str kms_key: If `encryption_type` is `KMS`, the ARN of the KMS key used.
        """
        pulumi.set(__self__, "encryption_type", encryption_type)
        pulumi.set(__self__, "kms_key", kms_key)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> str:
        """
        The encryption type to use for the repository, either `AES256` or `KMS`.
        """
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> str:
        """
        If `encryption_type` is `KMS`, the ARN of the KMS key used.
        """
        return pulumi.get(self, "kms_key")


@pulumi.output_type
class GetRepositoryImageScanningConfigurationResult(dict):
    def __init__(__self__, *,
                 scan_on_push: bool):
        """
        :param bool scan_on_push: Indicates whether images are scanned after being pushed to the repository.
        """
        pulumi.set(__self__, "scan_on_push", scan_on_push)

    @property
    @pulumi.getter(name="scanOnPush")
    def scan_on_push(self) -> bool:
        """
        Indicates whether images are scanned after being pushed to the repository.
        """
        return pulumi.get(self, "scan_on_push")


