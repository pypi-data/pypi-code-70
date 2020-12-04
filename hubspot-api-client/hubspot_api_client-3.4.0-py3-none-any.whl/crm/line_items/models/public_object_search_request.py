# coding: utf-8

"""
    Line Items

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.line_items.configuration import Configuration


class PublicObjectSearchRequest(object):
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
        'filter_groups': 'list[FilterGroup]',
        'sorts': 'list[str]',
        'query': 'str',
        'properties': 'list[str]',
        'limit': 'int',
        'after': 'int'
    }

    attribute_map = {
        'filter_groups': 'filterGroups',
        'sorts': 'sorts',
        'query': 'query',
        'properties': 'properties',
        'limit': 'limit',
        'after': 'after'
    }

    def __init__(self, filter_groups=None, sorts=None, query=None, properties=None, limit=None, after=None, local_vars_configuration=None):  # noqa: E501
        """PublicObjectSearchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filter_groups = None
        self._sorts = None
        self._query = None
        self._properties = None
        self._limit = None
        self._after = None
        self.discriminator = None

        self.filter_groups = filter_groups
        self.sorts = sorts
        if query is not None:
            self.query = query
        self.properties = properties
        self.limit = limit
        self.after = after

    @property
    def filter_groups(self):
        """Gets the filter_groups of this PublicObjectSearchRequest.  # noqa: E501


        :return: The filter_groups of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: list[FilterGroup]
        """
        return self._filter_groups

    @filter_groups.setter
    def filter_groups(self, filter_groups):
        """Sets the filter_groups of this PublicObjectSearchRequest.


        :param filter_groups: The filter_groups of this PublicObjectSearchRequest.  # noqa: E501
        :type: list[FilterGroup]
        """
        if self.local_vars_configuration.client_side_validation and filter_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_groups`, must not be `None`")  # noqa: E501

        self._filter_groups = filter_groups

    @property
    def sorts(self):
        """Gets the sorts of this PublicObjectSearchRequest.  # noqa: E501


        :return: The sorts of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        """Sets the sorts of this PublicObjectSearchRequest.


        :param sorts: The sorts of this PublicObjectSearchRequest.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and sorts is None:  # noqa: E501
            raise ValueError("Invalid value for `sorts`, must not be `None`")  # noqa: E501

        self._sorts = sorts

    @property
    def query(self):
        """Gets the query of this PublicObjectSearchRequest.  # noqa: E501


        :return: The query of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this PublicObjectSearchRequest.


        :param query: The query of this PublicObjectSearchRequest.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def properties(self):
        """Gets the properties of this PublicObjectSearchRequest.  # noqa: E501


        :return: The properties of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PublicObjectSearchRequest.


        :param properties: The properties of this PublicObjectSearchRequest.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def limit(self):
        """Gets the limit of this PublicObjectSearchRequest.  # noqa: E501


        :return: The limit of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PublicObjectSearchRequest.


        :param limit: The limit of this PublicObjectSearchRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def after(self):
        """Gets the after of this PublicObjectSearchRequest.  # noqa: E501


        :return: The after of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this PublicObjectSearchRequest.


        :param after: The after of this PublicObjectSearchRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and after is None:  # noqa: E501
            raise ValueError("Invalid value for `after`, must not be `None`")  # noqa: E501

        self._after = after

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
        if not isinstance(other, PublicObjectSearchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicObjectSearchRequest):
            return True

        return self.to_dict() != other.to_dict()
