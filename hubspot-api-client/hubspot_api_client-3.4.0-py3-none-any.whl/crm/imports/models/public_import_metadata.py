# coding: utf-8

"""
    CRM Imports

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.imports.configuration import Configuration


class PublicImportMetadata(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'object_lists': 'list[PublicObjectListRecord]',
        'counters': 'dict(str, int)',
        'file_ids': 'list[str]'
    }

    attribute_map = {
        'object_lists': 'objectLists',
        'counters': 'counters',
        'file_ids': 'fileIds'
    }

    def __init__(self, object_lists=None, counters=None, file_ids=None, local_vars_configuration=None):  # noqa: E501
        """PublicImportMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object_lists = None
        self._counters = None
        self._file_ids = None
        self.discriminator = None

        self.object_lists = object_lists
        self.counters = counters
        self.file_ids = file_ids

    @property
    def object_lists(self):
        """Gets the object_lists of this PublicImportMetadata.  # noqa: E501

        The lists containing the imported objects.  # noqa: E501

        :return: The object_lists of this PublicImportMetadata.  # noqa: E501
        :rtype: list[PublicObjectListRecord]
        """
        return self._object_lists

    @object_lists.setter
    def object_lists(self, object_lists):
        """Sets the object_lists of this PublicImportMetadata.

        The lists containing the imported objects.  # noqa: E501

        :param object_lists: The object_lists of this PublicImportMetadata.  # noqa: E501
        :type: list[PublicObjectListRecord]
        """
        if self.local_vars_configuration.client_side_validation and object_lists is None:  # noqa: E501
            raise ValueError("Invalid value for `object_lists`, must not be `None`")  # noqa: E501

        self._object_lists = object_lists

    @property
    def counters(self):
        """Gets the counters of this PublicImportMetadata.  # noqa: E501

        Summarized outcomes of each row a developer attempted to import into HubSpot.  # noqa: E501

        :return: The counters of this PublicImportMetadata.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._counters

    @counters.setter
    def counters(self, counters):
        """Sets the counters of this PublicImportMetadata.

        Summarized outcomes of each row a developer attempted to import into HubSpot.  # noqa: E501

        :param counters: The counters of this PublicImportMetadata.  # noqa: E501
        :type: dict(str, int)
        """
        if self.local_vars_configuration.client_side_validation and counters is None:  # noqa: E501
            raise ValueError("Invalid value for `counters`, must not be `None`")  # noqa: E501

        self._counters = counters

    @property
    def file_ids(self):
        """Gets the file_ids of this PublicImportMetadata.  # noqa: E501

        The IDs of files uploaded in the File Manager API.  # noqa: E501

        :return: The file_ids of this PublicImportMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids):
        """Sets the file_ids of this PublicImportMetadata.

        The IDs of files uploaded in the File Manager API.  # noqa: E501

        :param file_ids: The file_ids of this PublicImportMetadata.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and file_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `file_ids`, must not be `None`")  # noqa: E501

        self._file_ids = file_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicImportMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicImportMetadata):
            return True

        return self.to_dict() != other.to_dict()
