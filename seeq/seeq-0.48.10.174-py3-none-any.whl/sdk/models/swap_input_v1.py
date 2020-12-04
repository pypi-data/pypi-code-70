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


class SwapInputV1(object):
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
        'swap_in': 'str',
        'swap_out': 'str'
    }

    attribute_map = {
        'swap_in': 'swapIn',
        'swap_out': 'swapOut'
    }

    def __init__(self, swap_in=None, swap_out=None):
        """
        SwapInputV1 - a model defined in Swagger
        """

        self._swap_in = None
        self._swap_out = None

        if swap_in is not None:
          self.swap_in = swap_in
        if swap_out is not None:
          self.swap_out = swap_out

    @property
    def swap_in(self):
        """
        Gets the swap_in of this SwapInputV1.
        The ID of an asset to swap in. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :return: The swap_in of this SwapInputV1.
        :rtype: str
        """
        return self._swap_in

    @swap_in.setter
    def swap_in(self, swap_in):
        """
        Sets the swap_in of this SwapInputV1.
        The ID of an asset to swap in. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :param swap_in: The swap_in of this SwapInputV1.
        :type: str
        """

        self._swap_in = swap_in

    @property
    def swap_out(self):
        """
        Gets the swap_out of this SwapInputV1.
        The ID of an asset to swap out. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :return: The swap_out of this SwapInputV1.
        :rtype: str
        """
        return self._swap_out

    @swap_out.setter
    def swap_out(self, swap_out):
        """
        Sets the swap_out of this SwapInputV1.
        The ID of an asset to swap out. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :param swap_out: The swap_out of this SwapInputV1.
        :type: str
        """

        self._swap_out = swap_out

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
        if not isinstance(other, SwapInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
