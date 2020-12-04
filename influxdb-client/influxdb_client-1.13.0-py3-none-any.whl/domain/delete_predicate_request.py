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


class DeletePredicateRequest(object):
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
        'start': 'datetime',
        'stop': 'datetime',
        'predicate': 'str'
    }

    attribute_map = {
        'start': 'start',
        'stop': 'stop',
        'predicate': 'predicate'
    }

    def __init__(self, start=None, stop=None, predicate=None):  # noqa: E501,D401,D403
        """DeletePredicateRequest - a model defined in OpenAPI."""  # noqa: E501
        self._start = None
        self._stop = None
        self._predicate = None
        self.discriminator = None

        self.start = start
        self.stop = stop
        if predicate is not None:
            self.predicate = predicate

    @property
    def start(self):
        """Get the start of this DeletePredicateRequest.

        RFC3339Nano

        :return: The start of this DeletePredicateRequest.
        :rtype: datetime
        """  # noqa: E501
        return self._start

    @start.setter
    def start(self, start):
        """Set the start of this DeletePredicateRequest.

        RFC3339Nano

        :param start: The start of this DeletePredicateRequest.
        :type: datetime
        """  # noqa: E501
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        self._start = start

    @property
    def stop(self):
        """Get the stop of this DeletePredicateRequest.

        RFC3339Nano

        :return: The stop of this DeletePredicateRequest.
        :rtype: datetime
        """  # noqa: E501
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Set the stop of this DeletePredicateRequest.

        RFC3339Nano

        :param stop: The stop of this DeletePredicateRequest.
        :type: datetime
        """  # noqa: E501
        if stop is None:
            raise ValueError("Invalid value for `stop`, must not be `None`")  # noqa: E501
        self._stop = stop

    @property
    def predicate(self):
        """Get the predicate of this DeletePredicateRequest.

        InfluxQL-like delete statement

        :return: The predicate of this DeletePredicateRequest.
        :rtype: str
        """  # noqa: E501
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Set the predicate of this DeletePredicateRequest.

        InfluxQL-like delete statement

        :param predicate: The predicate of this DeletePredicateRequest.
        :type: str
        """  # noqa: E501
        self._predicate = predicate

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
        if not isinstance(other, DeletePredicateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
