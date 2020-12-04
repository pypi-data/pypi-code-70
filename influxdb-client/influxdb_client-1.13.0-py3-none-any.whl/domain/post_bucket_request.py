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


class PostBucketRequest(object):
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
        'org_id': 'str',
        'name': 'str',
        'description': 'str',
        'rp': 'str',
        'retention_rules': 'list[BucketRetentionRules]'
    }

    attribute_map = {
        'org_id': 'orgID',
        'name': 'name',
        'description': 'description',
        'rp': 'rp',
        'retention_rules': 'retentionRules'
    }

    def __init__(self, org_id=None, name=None, description=None, rp=None, retention_rules=None):  # noqa: E501,D401,D403
        """PostBucketRequest - a model defined in OpenAPI."""  # noqa: E501
        self._org_id = None
        self._name = None
        self._description = None
        self._rp = None
        self._retention_rules = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id
        self.name = name
        if description is not None:
            self.description = description
        if rp is not None:
            self.rp = rp
        self.retention_rules = retention_rules

    @property
    def org_id(self):
        """Get the org_id of this PostBucketRequest.

        :return: The org_id of this PostBucketRequest.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this PostBucketRequest.

        :param org_id: The org_id of this PostBucketRequest.
        :type: str
        """  # noqa: E501
        self._org_id = org_id

    @property
    def name(self):
        """Get the name of this PostBucketRequest.

        :return: The name of this PostBucketRequest.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this PostBucketRequest.

        :param name: The name of this PostBucketRequest.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this PostBucketRequest.

        :return: The description of this PostBucketRequest.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this PostBucketRequest.

        :param description: The description of this PostBucketRequest.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def rp(self):
        """Get the rp of this PostBucketRequest.

        :return: The rp of this PostBucketRequest.
        :rtype: str
        """  # noqa: E501
        return self._rp

    @rp.setter
    def rp(self, rp):
        """Set the rp of this PostBucketRequest.

        :param rp: The rp of this PostBucketRequest.
        :type: str
        """  # noqa: E501
        self._rp = rp

    @property
    def retention_rules(self):
        """Get the retention_rules of this PostBucketRequest.

        Rules to expire or retain data.  No rules means data never expires.

        :return: The retention_rules of this PostBucketRequest.
        :rtype: list[BucketRetentionRules]
        """  # noqa: E501
        return self._retention_rules

    @retention_rules.setter
    def retention_rules(self, retention_rules):
        """Set the retention_rules of this PostBucketRequest.

        Rules to expire or retain data.  No rules means data never expires.

        :param retention_rules: The retention_rules of this PostBucketRequest.
        :type: list[BucketRetentionRules]
        """  # noqa: E501
        if retention_rules is None:
            raise ValueError("Invalid value for `retention_rules`, must not be `None`")  # noqa: E501
        self._retention_rules = retention_rules

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
        if not isinstance(other, PostBucketRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
