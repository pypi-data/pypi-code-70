# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.49.07
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConfigurationInputV1(object):
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
        'configuration_options': 'list[ConfigurationOptionInputV1]',
        'dry_run': 'bool'
    }

    attribute_map = {
        'configuration_options': 'configurationOptions',
        'dry_run': 'dryRun'
    }

    def __init__(self, configuration_options=None, dry_run=False):
        """
        ConfigurationInputV1 - a model defined in Swagger
        """

        self._configuration_options = None
        self._dry_run = None

        if configuration_options is not None:
          self.configuration_options = configuration_options
        if dry_run is not None:
          self.dry_run = dry_run

    @property
    def configuration_options(self):
        """
        Gets the configuration_options of this ConfigurationInputV1.
        List of all configuration options to write.

        :return: The configuration_options of this ConfigurationInputV1.
        :rtype: list[ConfigurationOptionInputV1]
        """
        return self._configuration_options

    @configuration_options.setter
    def configuration_options(self, configuration_options):
        """
        Sets the configuration_options of this ConfigurationInputV1.
        List of all configuration options to write.

        :param configuration_options: The configuration_options of this ConfigurationInputV1.
        :type: list[ConfigurationOptionInputV1]
        """

        self._configuration_options = configuration_options

    @property
    def dry_run(self):
        """
        Gets the dry_run of this ConfigurationInputV1.
        Set to true to return a preview of the new config, but not save it

        :return: The dry_run of this ConfigurationInputV1.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """
        Sets the dry_run of this ConfigurationInputV1.
        Set to true to return a preview of the new config, but not save it

        :param dry_run: The dry_run of this ConfigurationInputV1.
        :type: bool
        """

        self._dry_run = dry_run

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
        if not isinstance(other, ConfigurationInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
