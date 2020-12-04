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


class FormulaParameterOutputV1(object):
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
        'formula': 'str',
        'item': 'ItemSearchPreviewV1',
        'name': 'str',
        'unbound': 'bool'
    }

    attribute_map = {
        'formula': 'formula',
        'item': 'item',
        'name': 'name',
        'unbound': 'unbound'
    }

    def __init__(self, formula=None, item=None, name=None, unbound=False):
        """
        FormulaParameterOutputV1 - a model defined in Swagger
        """

        self._formula = None
        self._item = None
        self._name = None
        self._unbound = None

        if formula is not None:
          self.formula = formula
        if item is not None:
          self.item = item
        if name is not None:
          self.name = name
        if unbound is not None:
          self.unbound = unbound

    @property
    def formula(self):
        """
        Gets the formula of this FormulaParameterOutputV1.
        The formula that defines this parameter if it is unbound or a formula parameter

        :return: The formula of this FormulaParameterOutputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this FormulaParameterOutputV1.
        The formula that defines this parameter if it is unbound or a formula parameter

        :param formula: The formula of this FormulaParameterOutputV1.
        :type: str
        """

        self._formula = formula

    @property
    def item(self):
        """
        Gets the item of this FormulaParameterOutputV1.
        The item that is the value of this parameter if it is a parameter that references an item

        :return: The item of this FormulaParameterOutputV1.
        :rtype: ItemSearchPreviewV1
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this FormulaParameterOutputV1.
        The item that is the value of this parameter if it is a parameter that references an item

        :param item: The item of this FormulaParameterOutputV1.
        :type: ItemSearchPreviewV1
        """

        self._item = item

    @property
    def name(self):
        """
        Gets the name of this FormulaParameterOutputV1.
        The name of the parameter as used in the formula without the '$' prefix.

        :return: The name of this FormulaParameterOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FormulaParameterOutputV1.
        The name of the parameter as used in the formula without the '$' prefix.

        :param name: The name of this FormulaParameterOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def unbound(self):
        """
        Gets the unbound of this FormulaParameterOutputV1.
        Indicate the value of this parameter will be provided at runtime

        :return: The unbound of this FormulaParameterOutputV1.
        :rtype: bool
        """
        return self._unbound

    @unbound.setter
    def unbound(self, unbound):
        """
        Sets the unbound of this FormulaParameterOutputV1.
        Indicate the value of this parameter will be provided at runtime

        :param unbound: The unbound of this FormulaParameterOutputV1.
        :type: bool
        """

        self._unbound = unbound

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
        if not isinstance(other, FormulaParameterOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
