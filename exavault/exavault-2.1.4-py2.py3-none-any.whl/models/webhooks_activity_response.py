# coding: utf-8

"""
    ExaVault API

    See our API reference documentation at https://www.exavault.com/developer/api-docs/  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@exavault.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WebhooksActivityResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'response_status': 'int',
        'total_results': 'int',
        'returned_results': 'int',
        'data': 'list[WebhooksActivityEntry]'
    }

    attribute_map = {
        'response_status': 'responseStatus',
        'total_results': 'totalResults',
        'returned_results': 'returnedResults',
        'data': 'data'
    }

    def __init__(self, response_status=None, total_results=None, returned_results=None, data=None):  # noqa: E501
        """WebhooksActivityResponse - a model defined in Swagger"""  # noqa: E501
        self._response_status = None
        self._total_results = None
        self._returned_results = None
        self._data = None
        self.discriminator = None
        if response_status is not None:
            self.response_status = response_status
        if total_results is not None:
            self.total_results = total_results
        if returned_results is not None:
            self.returned_results = returned_results
        if data is not None:
            self.data = data

    @property
    def response_status(self):
        """Gets the response_status of this WebhooksActivityResponse.  # noqa: E501

        Http status code of the response.  # noqa: E501

        :return: The response_status of this WebhooksActivityResponse.  # noqa: E501
        :rtype: int
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """Sets the response_status of this WebhooksActivityResponse.

        Http status code of the response.  # noqa: E501

        :param response_status: The response_status of this WebhooksActivityResponse.  # noqa: E501
        :type: int
        """

        self._response_status = response_status

    @property
    def total_results(self):
        """Gets the total_results of this WebhooksActivityResponse.  # noqa: E501

        Total results found.  # noqa: E501

        :return: The total_results of this WebhooksActivityResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this WebhooksActivityResponse.

        Total results found.  # noqa: E501

        :param total_results: The total_results of this WebhooksActivityResponse.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def returned_results(self):
        """Gets the returned_results of this WebhooksActivityResponse.  # noqa: E501

        Number of results returned.   # noqa: E501

        :return: The returned_results of this WebhooksActivityResponse.  # noqa: E501
        :rtype: int
        """
        return self._returned_results

    @returned_results.setter
    def returned_results(self, returned_results):
        """Sets the returned_results of this WebhooksActivityResponse.

        Number of results returned.   # noqa: E501

        :param returned_results: The returned_results of this WebhooksActivityResponse.  # noqa: E501
        :type: int
        """

        self._returned_results = returned_results

    @property
    def data(self):
        """Gets the data of this WebhooksActivityResponse.  # noqa: E501


        :return: The data of this WebhooksActivityResponse.  # noqa: E501
        :rtype: list[WebhooksActivityEntry]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WebhooksActivityResponse.


        :param data: The data of this WebhooksActivityResponse.  # noqa: E501
        :type: list[WebhooksActivityEntry]
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(WebhooksActivityResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhooksActivityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
