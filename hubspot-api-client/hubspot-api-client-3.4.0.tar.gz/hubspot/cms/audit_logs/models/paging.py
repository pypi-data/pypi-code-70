# coding: utf-8

"""
    CMS Audit Logs

    Use this endpoint to query audit logs of CMS changes that occurred on your HubSpot account.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.audit_logs.configuration import Configuration


class Paging(object):
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
        'next': 'NextPage'
    }

    attribute_map = {
        'next': 'next'
    }

    def __init__(self, next=None, local_vars_configuration=None):  # noqa: E501
        """Paging - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._next = None
        self.discriminator = None

        if next is not None:
            self.next = next

    @property
    def next(self):
        """Gets the next of this Paging.  # noqa: E501


        :return: The next of this Paging.  # noqa: E501
        :rtype: NextPage
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Paging.


        :param next: The next of this Paging.  # noqa: E501
        :type: NextPage
        """

        self._next = next

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
        if not isinstance(other, Paging):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Paging):
            return True

        return self.to_dict() != other.to_dict()
