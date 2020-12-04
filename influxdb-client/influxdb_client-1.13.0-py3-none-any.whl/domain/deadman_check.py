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
from influxdb_client.domain.check import Check


class DeadmanCheck(Check):
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
        'type': 'str',
        'time_since': 'str',
        'stale_time': 'str',
        'report_zero': 'bool',
        'level': 'CheckStatusLevel'
    }

    attribute_map = {
        'type': 'type',
        'time_since': 'timeSince',
        'stale_time': 'staleTime',
        'report_zero': 'reportZero',
        'level': 'level'
    }

    def __init__(self, type=None, time_since=None, stale_time=None, report_zero=None, level=None):  # noqa: E501,D401,D403
        """DeadmanCheck - a model defined in OpenAPI."""  # noqa: E501
        Check.__init__(self)  # noqa: E501

        self._type = None
        self._time_since = None
        self._stale_time = None
        self._report_zero = None
        self._level = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if time_since is not None:
            self.time_since = time_since
        if stale_time is not None:
            self.stale_time = stale_time
        if report_zero is not None:
            self.report_zero = report_zero
        if level is not None:
            self.level = level

    @property
    def type(self):
        """Get the type of this DeadmanCheck.

        :return: The type of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this DeadmanCheck.

        :param type: The type of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def time_since(self):
        """Get the time_since of this DeadmanCheck.

        String duration before deadman triggers.

        :return: The time_since of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._time_since

    @time_since.setter
    def time_since(self, time_since):
        """Set the time_since of this DeadmanCheck.

        String duration before deadman triggers.

        :param time_since: The time_since of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._time_since = time_since

    @property
    def stale_time(self):
        """Get the stale_time of this DeadmanCheck.

        String duration for time that a series is considered stale and should not trigger deadman.

        :return: The stale_time of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._stale_time

    @stale_time.setter
    def stale_time(self, stale_time):
        """Set the stale_time of this DeadmanCheck.

        String duration for time that a series is considered stale and should not trigger deadman.

        :param stale_time: The stale_time of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._stale_time = stale_time

    @property
    def report_zero(self):
        """Get the report_zero of this DeadmanCheck.

        If only zero values reported since time, trigger an alert

        :return: The report_zero of this DeadmanCheck.
        :rtype: bool
        """  # noqa: E501
        return self._report_zero

    @report_zero.setter
    def report_zero(self, report_zero):
        """Set the report_zero of this DeadmanCheck.

        If only zero values reported since time, trigger an alert

        :param report_zero: The report_zero of this DeadmanCheck.
        :type: bool
        """  # noqa: E501
        self._report_zero = report_zero

    @property
    def level(self):
        """Get the level of this DeadmanCheck.

        :return: The level of this DeadmanCheck.
        :rtype: CheckStatusLevel
        """  # noqa: E501
        return self._level

    @level.setter
    def level(self, level):
        """Set the level of this DeadmanCheck.

        :param level: The level of this DeadmanCheck.
        :type: CheckStatusLevel
        """  # noqa: E501
        self._level = level

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
        if not isinstance(other, DeadmanCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
