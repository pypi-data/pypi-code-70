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


class ExampleModel(object):
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
        'defined_in': 'str',
        'description': 'str',
        'formula': 'str',
        'order': 'int'
    }

    attribute_map = {
        'defined_in': 'definedIn',
        'description': 'description',
        'formula': 'formula',
        'order': 'order'
    }

    def __init__(self, defined_in=None, description=None, formula=None, order=None):
        """
        ExampleModel - a model defined in Swagger
        """

        self._defined_in = None
        self._description = None
        self._formula = None
        self._order = None

        if defined_in is not None:
          self.defined_in = defined_in
        if description is not None:
          self.description = description
        if formula is not None:
          self.formula = formula
        if order is not None:
          self.order = order

    @property
    def defined_in(self):
        """
        Gets the defined_in of this ExampleModel.

        :return: The defined_in of this ExampleModel.
        :rtype: str
        """
        return self._defined_in

    @defined_in.setter
    def defined_in(self, defined_in):
        """
        Sets the defined_in of this ExampleModel.

        :param defined_in: The defined_in of this ExampleModel.
        :type: str
        """

        self._defined_in = defined_in

    @property
    def description(self):
        """
        Gets the description of this ExampleModel.

        :return: The description of this ExampleModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExampleModel.

        :param description: The description of this ExampleModel.
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """
        Gets the formula of this ExampleModel.

        :return: The formula of this ExampleModel.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this ExampleModel.

        :param formula: The formula of this ExampleModel.
        :type: str
        """

        self._formula = formula

    @property
    def order(self):
        """
        Gets the order of this ExampleModel.

        :return: The order of this ExampleModel.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this ExampleModel.

        :param order: The order of this ExampleModel.
        :type: int
        """

        self._order = order

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
        if not isinstance(other, ExampleModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
