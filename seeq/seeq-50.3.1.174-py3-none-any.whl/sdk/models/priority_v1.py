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


class PriorityV1(object):
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
        'color': 'str',
        'level': 'int',
        'name': 'str'
    }

    attribute_map = {
        'color': 'color',
        'level': 'level',
        'name': 'name'
    }

    def __init__(self, color=None, level=None, name=None):
        """
        PriorityV1 - a model defined in Swagger
        """

        self._color = None
        self._level = None
        self._name = None

        if color is not None:
          self.color = color
        if level is not None:
          self.level = level
        if name is not None:
          self.name = name

    @property
    def color(self):
        """
        Gets the color of this PriorityV1.
        A hex code (including pound sign) representing the color assigned to this priority

        :return: The color of this PriorityV1.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this PriorityV1.
        A hex code (including pound sign) representing the color assigned to this priority

        :param color: The color of this PriorityV1.
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")

        self._color = color

    @property
    def level(self):
        """
        Gets the level of this PriorityV1.
        An integer representing the priority level. 0 is used for neutral, positive numbers are used for high thresholds and negative numbers for low thresholds

        :return: The level of this PriorityV1.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this PriorityV1.
        An integer representing the priority level. 0 is used for neutral, positive numbers are used for high thresholds and negative numbers for low thresholds

        :param level: The level of this PriorityV1.
        :type: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")

        self._level = level

    @property
    def name(self):
        """
        Gets the name of this PriorityV1.
        The name of this priority

        :return: The name of this PriorityV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PriorityV1.
        The name of this priority

        :param name: The name of this PriorityV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, PriorityV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
