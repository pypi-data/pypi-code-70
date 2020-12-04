# coding: utf-8

"""
    Tickets

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.tickets.configuration import Configuration


class Error(object):
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
        'correlation_id': 'str',
        'category': 'str',
        'sub_category': 'str',
        'errors': 'list[ErrorDetail]',
        'context': 'dict(str, list[str])',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'message': 'message',
        'correlation_id': 'correlationId',
        'category': 'category',
        'sub_category': 'subCategory',
        'errors': 'errors',
        'context': 'context',
        'links': 'links'
    }

    def __init__(self, message=None, correlation_id=None, category=None, sub_category=None, errors=None, context=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._correlation_id = None
        self._category = None
        self._sub_category = None
        self._errors = None
        self._context = None
        self._links = None
        self.discriminator = None

        self.message = message
        self.correlation_id = correlation_id
        self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if errors is not None:
            self.errors = errors
        if context is not None:
            self.context = context
        if links is not None:
            self.links = links

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        A human readable message describing the error along with remediation steps where appropriate  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        A human readable message describing the error along with remediation steps where appropriate  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def correlation_id(self):
        """Gets the correlation_id of this Error.  # noqa: E501

        A unique identifier for the request. Include this value with any error reports or support tickets  # noqa: E501

        :return: The correlation_id of this Error.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this Error.

        A unique identifier for the request. Include this value with any error reports or support tickets  # noqa: E501

        :param correlation_id: The correlation_id of this Error.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and correlation_id is None:  # noqa: E501
            raise ValueError("Invalid value for `correlation_id`, must not be `None`")  # noqa: E501

        self._correlation_id = correlation_id

    @property
    def category(self):
        """Gets the category of this Error.  # noqa: E501

        The error category  # noqa: E501

        :return: The category of this Error.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Error.

        The error category  # noqa: E501

        :param category: The category of this Error.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this Error.  # noqa: E501

        A specific category that contains more specific detail about the error  # noqa: E501

        :return: The sub_category of this Error.  # noqa: E501
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this Error.

        A specific category that contains more specific detail about the error  # noqa: E501

        :param sub_category: The sub_category of this Error.  # noqa: E501
        :type: str
        """

        self._sub_category = sub_category

    @property
    def errors(self):
        """Gets the errors of this Error.  # noqa: E501

        further information about the error  # noqa: E501

        :return: The errors of this Error.  # noqa: E501
        :rtype: list[ErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Error.

        further information about the error  # noqa: E501

        :param errors: The errors of this Error.  # noqa: E501
        :type: list[ErrorDetail]
        """

        self._errors = errors

    @property
    def context(self):
        """Gets the context of this Error.  # noqa: E501

        Context about the error condition  # noqa: E501

        :return: The context of this Error.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this Error.

        Context about the error condition  # noqa: E501

        :param context: The context of this Error.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._context = context

    @property
    def links(self):
        """Gets the links of this Error.  # noqa: E501

        A map of link names to associated URIs containing documentation about the error or recommended remediation steps  # noqa: E501

        :return: The links of this Error.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Error.

        A map of link names to associated URIs containing documentation about the error or recommended remediation steps  # noqa: E501

        :param links: The links of this Error.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

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
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
