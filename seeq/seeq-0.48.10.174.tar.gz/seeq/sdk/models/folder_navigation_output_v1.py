# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.48.10-BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FolderNavigationOutputV1(object):
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
        'id': 'str',
        'name': 'str',
        'parent_id': 'str',
        'subfolders': 'list[FolderNavigationOutputV1]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent_id': 'parentId',
        'subfolders': 'subfolders'
    }

    def __init__(self, id=None, name=None, parent_id=None, subfolders=None):
        """
        FolderNavigationOutputV1 - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._parent_id = None
        self._subfolders = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if parent_id is not None:
          self.parent_id = parent_id
        if subfolders is not None:
          self.subfolders = subfolders

    @property
    def id(self):
        """
        Gets the id of this FolderNavigationOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this FolderNavigationOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FolderNavigationOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this FolderNavigationOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FolderNavigationOutputV1.
        The human readable name

        :return: The name of this FolderNavigationOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FolderNavigationOutputV1.
        The human readable name

        :param name: The name of this FolderNavigationOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parent_id(self):
        """
        Gets the parent_id of this FolderNavigationOutputV1.
        The ID of the hierarchy parent of this item. May be null if it's a root-level item

        :return: The parent_id of this FolderNavigationOutputV1.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this FolderNavigationOutputV1.
        The ID of the hierarchy parent of this item. May be null if it's a root-level item

        :param parent_id: The parent_id of this FolderNavigationOutputV1.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def subfolders(self):
        """
        Gets the subfolders of this FolderNavigationOutputV1.
        The list of subfolders

        :return: The subfolders of this FolderNavigationOutputV1.
        :rtype: list[FolderNavigationOutputV1]
        """
        return self._subfolders

    @subfolders.setter
    def subfolders(self, subfolders):
        """
        Sets the subfolders of this FolderNavigationOutputV1.
        The list of subfolders

        :param subfolders: The subfolders of this FolderNavigationOutputV1.
        :type: list[FolderNavigationOutputV1]
        """

        self._subfolders = subfolders

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
        if not isinstance(other, FolderNavigationOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
