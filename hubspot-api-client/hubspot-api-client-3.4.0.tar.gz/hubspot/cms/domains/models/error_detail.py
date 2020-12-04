# coding: utf-8

"""
    Domains

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.domains.configuration import Configuration


class ErrorDetail(object):
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
        'message': 'str',
        '_in': 'str',
        'code': 'str',
        'sub_category': 'str',
        'context': 'dict(str, list[str])'
    }

    attribute_map = {
        'message': 'message',
        '_in': 'in',
        'code': 'code',
        'sub_category': 'subCategory',
        'context': 'context'
    }

    def __init__(self, message=None, _in=None, code=None, sub_category=None, context=None, local_vars_configuration=None):  # noqa: E501
        """ErrorDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self.__in = None
        self._code = None
        self._sub_category = None
        self._context = None
        self.discriminator = None

        self.message = message
        if _in is not None:
            self._in = _in
        if code is not None:
            self.code = code
        if sub_category is not None:
            self.sub_category = sub_category
        if context is not None:
            self.context = context

    @property
    def message(self):
        """Gets the message of this ErrorDetail.  # noqa: E501

        A human readable message describing the error along with remediation steps where appropriate  # noqa: E501

        :return: The message of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorDetail.

        A human readable message describing the error along with remediation steps where appropriate  # noqa: E501

        :param message: The message of this ErrorDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def _in(self):
        """Gets the _in of this ErrorDetail.  # noqa: E501

        The name of the field or parameter in which the error was found.  # noqa: E501

        :return: The _in of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this ErrorDetail.

        The name of the field or parameter in which the error was found.  # noqa: E501

        :param _in: The _in of this ErrorDetail.  # noqa: E501
        :type: str
        """

        self.__in = _in

    @property
    def code(self):
        """Gets the code of this ErrorDetail.  # noqa: E501

        The status code associated with the error detail  # noqa: E501

        :return: The code of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorDetail.

        The status code associated with the error detail  # noqa: E501

        :param code: The code of this ErrorDetail.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def sub_category(self):
        """Gets the sub_category of this ErrorDetail.  # noqa: E501

        A specific category that contains more specific detail about the error  # noqa: E501

        :return: The sub_category of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this ErrorDetail.

        A specific category that contains more specific detail about the error  # noqa: E501

        :param sub_category: The sub_category of this ErrorDetail.  # noqa: E501
        :type: str
        """

        self._sub_category = sub_category

    @property
    def context(self):
        """Gets the context of this ErrorDetail.  # noqa: E501

        Context about the error condition  # noqa: E501

        :return: The context of this ErrorDetail.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ErrorDetail.

        Context about the error condition  # noqa: E501

        :param context: The context of this ErrorDetail.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._context = context

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
        if not isinstance(other, ErrorDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorDetail):
            return True

        return self.to_dict() != other.to_dict()
