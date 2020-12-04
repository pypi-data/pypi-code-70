# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 50.3.1-BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DatasourceCleanUpInputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'item_data_id_exclude_regex_filter': 'str',
        'item_data_id_regex_filter': 'str',
        'item_name_exclude_regex_filter': 'str',
        'item_name_regex_filter': 'str',
        'item_type_filter': 'list[str]',
        'sync_token': 'str'
    }

    attribute_map = {
        'item_data_id_exclude_regex_filter': 'itemDataIdExcludeRegexFilter',
        'item_data_id_regex_filter': 'itemDataIdRegexFilter',
        'item_name_exclude_regex_filter': 'itemNameExcludeRegexFilter',
        'item_name_regex_filter': 'itemNameRegexFilter',
        'item_type_filter': 'itemTypeFilter',
        'sync_token': 'syncToken'
    }

    def __init__(self, item_data_id_exclude_regex_filter=None, item_data_id_regex_filter=None, item_name_exclude_regex_filter=None, item_name_regex_filter=None, item_type_filter=None, sync_token=None):
        """
        DatasourceCleanUpInputV1 - a model defined in Swagger
        """

        self._item_data_id_exclude_regex_filter = None
        self._item_data_id_regex_filter = None
        self._item_name_exclude_regex_filter = None
        self._item_name_regex_filter = None
        self._item_type_filter = None
        self._sync_token = None

        if item_data_id_exclude_regex_filter is not None:
          self.item_data_id_exclude_regex_filter = item_data_id_exclude_regex_filter
        if item_data_id_regex_filter is not None:
          self.item_data_id_regex_filter = item_data_id_regex_filter
        if item_name_exclude_regex_filter is not None:
          self.item_name_exclude_regex_filter = item_name_exclude_regex_filter
        if item_name_regex_filter is not None:
          self.item_name_regex_filter = item_name_regex_filter
        if item_type_filter is not None:
          self.item_type_filter = item_type_filter
        if sync_token is not None:
          self.sync_token = sync_token

    @property
    def item_data_id_exclude_regex_filter(self):
        """
        Gets the item_data_id_exclude_regex_filter of this DatasourceCleanUpInputV1.
        When set, the items having the DataId matching the RegEx will be excluded from cleanup process.

        :return: The item_data_id_exclude_regex_filter of this DatasourceCleanUpInputV1.
        :rtype: str
        """
        return self._item_data_id_exclude_regex_filter

    @item_data_id_exclude_regex_filter.setter
    def item_data_id_exclude_regex_filter(self, item_data_id_exclude_regex_filter):
        """
        Sets the item_data_id_exclude_regex_filter of this DatasourceCleanUpInputV1.
        When set, the items having the DataId matching the RegEx will be excluded from cleanup process.

        :param item_data_id_exclude_regex_filter: The item_data_id_exclude_regex_filter of this DatasourceCleanUpInputV1.
        :type: str
        """

        self._item_data_id_exclude_regex_filter = item_data_id_exclude_regex_filter

    @property
    def item_data_id_regex_filter(self):
        """
        Gets the item_data_id_regex_filter of this DatasourceCleanUpInputV1.
        When set, only items having the DataId matching the RegEx will be included in cleanup process.

        :return: The item_data_id_regex_filter of this DatasourceCleanUpInputV1.
        :rtype: str
        """
        return self._item_data_id_regex_filter

    @item_data_id_regex_filter.setter
    def item_data_id_regex_filter(self, item_data_id_regex_filter):
        """
        Sets the item_data_id_regex_filter of this DatasourceCleanUpInputV1.
        When set, only items having the DataId matching the RegEx will be included in cleanup process.

        :param item_data_id_regex_filter: The item_data_id_regex_filter of this DatasourceCleanUpInputV1.
        :type: str
        """

        self._item_data_id_regex_filter = item_data_id_regex_filter

    @property
    def item_name_exclude_regex_filter(self):
        """
        Gets the item_name_exclude_regex_filter of this DatasourceCleanUpInputV1.
        When set, the items having the name matching the RegEx will be excluded from cleanup process.

        :return: The item_name_exclude_regex_filter of this DatasourceCleanUpInputV1.
        :rtype: str
        """
        return self._item_name_exclude_regex_filter

    @item_name_exclude_regex_filter.setter
    def item_name_exclude_regex_filter(self, item_name_exclude_regex_filter):
        """
        Sets the item_name_exclude_regex_filter of this DatasourceCleanUpInputV1.
        When set, the items having the name matching the RegEx will be excluded from cleanup process.

        :param item_name_exclude_regex_filter: The item_name_exclude_regex_filter of this DatasourceCleanUpInputV1.
        :type: str
        """

        self._item_name_exclude_regex_filter = item_name_exclude_regex_filter

    @property
    def item_name_regex_filter(self):
        """
        Gets the item_name_regex_filter of this DatasourceCleanUpInputV1.
        When set, only items having the name matching the RegEx will be included in cleanup process.

        :return: The item_name_regex_filter of this DatasourceCleanUpInputV1.
        :rtype: str
        """
        return self._item_name_regex_filter

    @item_name_regex_filter.setter
    def item_name_regex_filter(self, item_name_regex_filter):
        """
        Sets the item_name_regex_filter of this DatasourceCleanUpInputV1.
        When set, only items having the name matching the RegEx will be included in cleanup process.

        :param item_name_regex_filter: The item_name_regex_filter of this DatasourceCleanUpInputV1.
        :type: str
        """

        self._item_name_regex_filter = item_name_regex_filter

    @property
    def item_type_filter(self):
        """
        Gets the item_type_filter of this DatasourceCleanUpInputV1.
        List of item types on which cleanup will be done. When no filter is specified (empty or null list), all types of items will be included in the cleanup process.

        :return: The item_type_filter of this DatasourceCleanUpInputV1.
        :rtype: list[str]
        """
        return self._item_type_filter

    @item_type_filter.setter
    def item_type_filter(self, item_type_filter):
        """
        Sets the item_type_filter of this DatasourceCleanUpInputV1.
        List of item types on which cleanup will be done. When no filter is specified (empty or null list), all types of items will be included in the cleanup process.

        :param item_type_filter: The item_type_filter of this DatasourceCleanUpInputV1.
        :type: list[str]
        """

        self._item_type_filter = item_type_filter

    @property
    def sync_token(self):
        """
        Gets the sync_token of this DatasourceCleanUpInputV1.
        The sync token to check on each item

        :return: The sync_token of this DatasourceCleanUpInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this DatasourceCleanUpInputV1.
        The sync token to check on each item

        :param sync_token: The sync_token of this DatasourceCleanUpInputV1.
        :type: str
        """
        if sync_token is None:
            raise ValueError("Invalid value for `sync_token`, must not be `None`")

        self._sync_token = sync_token

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DatasourceCleanUpInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
