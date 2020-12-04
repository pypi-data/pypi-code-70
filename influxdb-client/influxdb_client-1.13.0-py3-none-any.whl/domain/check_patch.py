# coding: utf-8

"""
Influx API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 0.1.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CheckPatch(object):
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
        'name': 'str',
        'description': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, name=None, description=None, status=None):  # noqa: E501,D401,D403
        """CheckPatch - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._description = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Get the name of this CheckPatch.

        :return: The name of this CheckPatch.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this CheckPatch.

        :param name: The name of this CheckPatch.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this CheckPatch.

        :return: The description of this CheckPatch.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this CheckPatch.

        :param description: The description of this CheckPatch.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def status(self):
        """Get the status of this CheckPatch.

        :return: The status of this CheckPatch.
        :rtype: str
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this CheckPatch.

        :param status: The status of this CheckPatch.
        :type: str
        """  # noqa: E501
        self._status = status

    def to_dict(self):
        """Return the model properties as a dict."""
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, CheckPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
