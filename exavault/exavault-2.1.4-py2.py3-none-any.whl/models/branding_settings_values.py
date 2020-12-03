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

class BrandingSettingsValues(object):
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
        'company_name': 'str',
        'custom_email': 'str',
        'theme': 'str'
    }

    attribute_map = {
        'company_name': 'companyName',
        'custom_email': 'customEmail',
        'theme': 'theme'
    }

    def __init__(self, company_name=None, custom_email=None, theme=None):  # noqa: E501
        """BrandingSettingsValues - a model defined in Swagger"""  # noqa: E501
        self._company_name = None
        self._custom_email = None
        self._theme = None
        self.discriminator = None
        if company_name is not None:
            self.company_name = company_name
        if custom_email is not None:
            self.custom_email = custom_email
        if theme is not None:
            self.theme = theme

    @property
    def company_name(self):
        """Gets the company_name of this BrandingSettingsValues.  # noqa: E501

        Custom company name to include in copyright and title bar.  # noqa: E501

        :return: The company_name of this BrandingSettingsValues.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this BrandingSettingsValues.

        Custom company name to include in copyright and title bar.  # noqa: E501

        :param company_name: The company_name of this BrandingSettingsValues.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def custom_email(self):
        """Gets the custom_email of this BrandingSettingsValues.  # noqa: E501

        Address to use as sender of email messages generated by ExaVault  # noqa: E501

        :return: The custom_email of this BrandingSettingsValues.  # noqa: E501
        :rtype: str
        """
        return self._custom_email

    @custom_email.setter
    def custom_email(self, custom_email):
        """Sets the custom_email of this BrandingSettingsValues.

        Address to use as sender of email messages generated by ExaVault  # noqa: E501

        :param custom_email: The custom_email of this BrandingSettingsValues.  # noqa: E501
        :type: str
        """

        self._custom_email = custom_email

    @property
    def theme(self):
        """Gets the theme of this BrandingSettingsValues.  # noqa: E501

        Color scheme for web file manager. Valid options are **default**, **light** and **dark**  # noqa: E501

        :return: The theme of this BrandingSettingsValues.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this BrandingSettingsValues.

        Color scheme for web file manager. Valid options are **default**, **light** and **dark**  # noqa: E501

        :param theme: The theme of this BrandingSettingsValues.  # noqa: E501
        :type: str
        """

        self._theme = theme

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
        if issubclass(BrandingSettingsValues, dict):
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
        if not isinstance(other, BrandingSettingsValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
