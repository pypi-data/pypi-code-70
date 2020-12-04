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


class DecimalPlaces(object):
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
        'is_enforced': 'bool',
        'digits': 'int'
    }

    attribute_map = {
        'is_enforced': 'isEnforced',
        'digits': 'digits'
    }

    def __init__(self, is_enforced=None, digits=None):  # noqa: E501,D401,D403
        """DecimalPlaces - a model defined in OpenAPI."""  # noqa: E501
        self._is_enforced = None
        self._digits = None
        self.discriminator = None

        if is_enforced is not None:
            self.is_enforced = is_enforced
        if digits is not None:
            self.digits = digits

    @property
    def is_enforced(self):
        """Get the is_enforced of this DecimalPlaces.

        Indicates whether decimal point setting should be enforced

        :return: The is_enforced of this DecimalPlaces.
        :rtype: bool
        """  # noqa: E501
        return self._is_enforced

    @is_enforced.setter
    def is_enforced(self, is_enforced):
        """Set the is_enforced of this DecimalPlaces.

        Indicates whether decimal point setting should be enforced

        :param is_enforced: The is_enforced of this DecimalPlaces.
        :type: bool
        """  # noqa: E501
        self._is_enforced = is_enforced

    @property
    def digits(self):
        """Get the digits of this DecimalPlaces.

        The number of digits after decimal to display

        :return: The digits of this DecimalPlaces.
        :rtype: int
        """  # noqa: E501
        return self._digits

    @digits.setter
    def digits(self, digits):
        """Set the digits of this DecimalPlaces.

        The number of digits after decimal to display

        :param digits: The digits of this DecimalPlaces.
        :type: int
        """  # noqa: E501
        self._digits = digits

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
        if not isinstance(other, DecimalPlaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
