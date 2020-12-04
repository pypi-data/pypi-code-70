# coding: utf-8

"""
    CRM Objects

    CRM objects such as companies, contacts, deals, line items, products, tickets, and quotes are standard objects in HubSpot’s CRM. These core building blocks support custom properties, store critical information, and play a central role in the HubSpot application.  ## Supported Object Types  This API provides access to collections of CRM objects, which return a map of property names to values. Each object type has its own set of default properties, which can be found by exploring the [CRM Object Properties API](https://developers.hubspot.com/docs/methods/crm-properties/crm-properties-overview).  |Object Type |Properties returned by default | |--|--| | `companies` | `name`, `domain` | | `contacts` | `firstname`, `lastname`, `email` | | `deals` | `dealname`, `amount`, `closedate`, `pipeline`, `dealstage` | | `products` | `name`, `description`, `price` | | `tickets` | `content`, `hs_pipeline`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_priority`, `subject` |  Find a list of all properties for an object type using the [CRM Object Properties](https://developers.hubspot.com/docs/methods/crm-properties/get-properties) API. e.g. `GET https://api.hubapi.com/properties/v2/companies/properties`. Change the properties returned in the response using the `properties` array in the request body.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.objects.configuration import Configuration


class StandardError(object):
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
        'status': 'str',
        'id': 'str',
        'category': 'ErrorCategory',
        'sub_category': 'object',
        'message': 'str',
        'errors': 'list[ErrorDetail]',
        'context': 'dict(str, list[str])',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'category': 'category',
        'sub_category': 'subCategory',
        'message': 'message',
        'errors': 'errors',
        'context': 'context',
        'links': 'links'
    }

    def __init__(self, status=None, id=None, category=None, sub_category=None, message=None, errors=None, context=None, links=None, local_vars_configuration=None):  # noqa: E501
        """StandardError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._id = None
        self._category = None
        self._sub_category = None
        self._message = None
        self._errors = None
        self._context = None
        self._links = None
        self.discriminator = None

        self.status = status
        if id is not None:
            self.id = id
        self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        self.message = message
        self.errors = errors
        self.context = context
        self.links = links

    @property
    def status(self):
        """Gets the status of this StandardError.  # noqa: E501


        :return: The status of this StandardError.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StandardError.


        :param status: The status of this StandardError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def id(self):
        """Gets the id of this StandardError.  # noqa: E501


        :return: The id of this StandardError.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StandardError.


        :param id: The id of this StandardError.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this StandardError.  # noqa: E501


        :return: The category of this StandardError.  # noqa: E501
        :rtype: ErrorCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this StandardError.


        :param category: The category of this StandardError.  # noqa: E501
        :type: ErrorCategory
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this StandardError.  # noqa: E501


        :return: The sub_category of this StandardError.  # noqa: E501
        :rtype: object
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this StandardError.


        :param sub_category: The sub_category of this StandardError.  # noqa: E501
        :type: object
        """

        self._sub_category = sub_category

    @property
    def message(self):
        """Gets the message of this StandardError.  # noqa: E501


        :return: The message of this StandardError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this StandardError.


        :param message: The message of this StandardError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this StandardError.  # noqa: E501


        :return: The errors of this StandardError.  # noqa: E501
        :rtype: list[ErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this StandardError.


        :param errors: The errors of this StandardError.  # noqa: E501
        :type: list[ErrorDetail]
        """
        if self.local_vars_configuration.client_side_validation and errors is None:  # noqa: E501
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def context(self):
        """Gets the context of this StandardError.  # noqa: E501


        :return: The context of this StandardError.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this StandardError.


        :param context: The context of this StandardError.  # noqa: E501
        :type: dict(str, list[str])
        """
        if self.local_vars_configuration.client_side_validation and context is None:  # noqa: E501
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def links(self):
        """Gets the links of this StandardError.  # noqa: E501


        :return: The links of this StandardError.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StandardError.


        :param links: The links of this StandardError.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, StandardError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StandardError):
            return True

        return self.to_dict() != other.to_dict()
