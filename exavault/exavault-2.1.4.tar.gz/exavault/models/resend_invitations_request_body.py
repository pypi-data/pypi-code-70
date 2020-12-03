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

class ResendInvitationsRequestBody(object):
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
        'recipient_id': 'int'
    }

    attribute_map = {
        'recipient_id': 'recipientId'
    }

    def __init__(self, recipient_id=None):  # noqa: E501
        """ResendInvitationsRequestBody - a model defined in Swagger"""  # noqa: E501
        self._recipient_id = None
        self.discriminator = None
        if recipient_id is not None:
            self.recipient_id = recipient_id

    @property
    def recipient_id(self):
        """Gets the recipient_id of this ResendInvitationsRequestBody.  # noqa: E501

        ID number of recipient to send a new invitation to.  # noqa: E501

        :return: The recipient_id of this ResendInvitationsRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this ResendInvitationsRequestBody.

        ID number of recipient to send a new invitation to.  # noqa: E501

        :param recipient_id: The recipient_id of this ResendInvitationsRequestBody.  # noqa: E501
        :type: int
        """

        self._recipient_id = recipient_id

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
        if issubclass(ResendInvitationsRequestBody, dict):
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
        if not isinstance(other, ResendInvitationsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
