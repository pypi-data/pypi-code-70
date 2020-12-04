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


class TreemapItemOutputV1(object):
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
        'asset': 'AssetOutputV1',
        'display_scalars': 'list[ScalarValueOutputV1]',
        'is_leaf_asset': 'bool',
        'is_uncertain': 'bool',
        'priority': 'int',
        'size': 'object'
    }

    attribute_map = {
        'asset': 'asset',
        'display_scalars': 'displayScalars',
        'is_leaf_asset': 'isLeafAsset',
        'is_uncertain': 'isUncertain',
        'priority': 'priority',
        'size': 'size'
    }

    def __init__(self, asset=None, display_scalars=None, is_leaf_asset=False, is_uncertain=False, priority=None, size=None):
        """
        TreemapItemOutputV1 - a model defined in Swagger
        """

        self._asset = None
        self._display_scalars = None
        self._is_leaf_asset = None
        self._is_uncertain = None
        self._priority = None
        self._size = None

        if asset is not None:
          self.asset = asset
        if display_scalars is not None:
          self.display_scalars = display_scalars
        if is_leaf_asset is not None:
          self.is_leaf_asset = is_leaf_asset
        if is_uncertain is not None:
          self.is_uncertain = is_uncertain
        if priority is not None:
          self.priority = priority
        if size is not None:
          self.size = size

    @property
    def asset(self):
        """
        Gets the asset of this TreemapItemOutputV1.
        The asset or asset tree described by this item

        :return: The asset of this TreemapItemOutputV1.
        :rtype: AssetOutputV1
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """
        Sets the asset of this TreemapItemOutputV1.
        The asset or asset tree described by this item

        :param asset: The asset of this TreemapItemOutputV1.
        :type: AssetOutputV1
        """

        self._asset = asset

    @property
    def display_scalars(self):
        """
        Gets the display_scalars of this TreemapItemOutputV1.
        The display scalars evaluated for this asset

        :return: The display_scalars of this TreemapItemOutputV1.
        :rtype: list[ScalarValueOutputV1]
        """
        return self._display_scalars

    @display_scalars.setter
    def display_scalars(self, display_scalars):
        """
        Sets the display_scalars of this TreemapItemOutputV1.
        The display scalars evaluated for this asset

        :param display_scalars: The display_scalars of this TreemapItemOutputV1.
        :type: list[ScalarValueOutputV1]
        """

        self._display_scalars = display_scalars

    @property
    def is_leaf_asset(self):
        """
        Gets the is_leaf_asset of this TreemapItemOutputV1.
        True if this item is an asset; false if this item contains aggregate info for an asset tree

        :return: The is_leaf_asset of this TreemapItemOutputV1.
        :rtype: bool
        """
        return self._is_leaf_asset

    @is_leaf_asset.setter
    def is_leaf_asset(self, is_leaf_asset):
        """
        Sets the is_leaf_asset of this TreemapItemOutputV1.
        True if this item is an asset; false if this item contains aggregate info for an asset tree

        :param is_leaf_asset: The is_leaf_asset of this TreemapItemOutputV1.
        :type: bool
        """

        self._is_leaf_asset = is_leaf_asset

    @property
    def is_uncertain(self):
        """
        Gets the is_uncertain of this TreemapItemOutputV1.
        True if this item's priority is uncertain

        :return: The is_uncertain of this TreemapItemOutputV1.
        :rtype: bool
        """
        return self._is_uncertain

    @is_uncertain.setter
    def is_uncertain(self, is_uncertain):
        """
        Sets the is_uncertain of this TreemapItemOutputV1.
        True if this item's priority is uncertain

        :param is_uncertain: The is_uncertain of this TreemapItemOutputV1.
        :type: bool
        """

        self._is_uncertain = is_uncertain

    @property
    def priority(self):
        """
        Gets the priority of this TreemapItemOutputV1.
        The highest priority condition met by this asset or asset tree. The highest priority condition possible has a value of 0; when no conditions are met, -1 is returned. 

        :return: The priority of this TreemapItemOutputV1.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this TreemapItemOutputV1.
        The highest priority condition met by this asset or asset tree. The highest priority condition possible has a value of 0; when no conditions are met, -1 is returned. 

        :param priority: The priority of this TreemapItemOutputV1.
        :type: int
        """

        self._priority = priority

    @property
    def size(self):
        """
        Gets the size of this TreemapItemOutputV1.
        The relative size of this asset or asset tree

        :return: The size of this TreemapItemOutputV1.
        :rtype: object
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this TreemapItemOutputV1.
        The relative size of this asset or asset tree

        :param size: The size of this TreemapItemOutputV1.
        :type: object
        """

        self._size = size

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
        if not isinstance(other, TreemapItemOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
