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


class SendLogsInputV1(object):
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
        'description': 'str',
        'email': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'email': 'email',
        'name': 'name'
    }

    def __init__(self, description=None, email=None, name=None):
        """
        SendLogsInputV1 - a model defined in Swagger
        """

        self._description = None
        self._email = None
        self._name = None

        if description is not None:
          self.description = description
        if email is not None:
          self.email = email
        if name is not None:
          self.name = name

    @property
    def description(self):
        """
        Gets the description of this SendLogsInputV1.
        The description to be sent with the logs

        :return: The description of this SendLogsInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SendLogsInputV1.
        The description to be sent with the logs

        :param description: The description of this SendLogsInputV1.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def email(self):
        """
        Gets the email of this SendLogsInputV1.
        The log sender's email

        :return: The email of this SendLogsInputV1.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SendLogsInputV1.
        The log sender's email

        :param email: The email of this SendLogsInputV1.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def name(self):
        """
        Gets the name of this SendLogsInputV1.
        The log sender's name

        :return: The name of this SendLogsInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SendLogsInputV1.
        The log sender's name

        :param name: The name of this SendLogsInputV1.
        :type: str
        """

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
        if not isinstance(other, SendLogsInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
