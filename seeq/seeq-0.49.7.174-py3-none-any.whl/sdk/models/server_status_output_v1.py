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


class ServerStatusOutputV1(object):
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
        'configuration_options': 'list[ConfigurationOptionOutputSimpleV1]',
        'default_max_capsule_duration': 'ScalarValueOutputV1',
        'default_max_interpolation': 'ScalarValueOutputV1',
        'priorities': 'list[PriorityV1]',
        'server_specs': 'list[ServerSpecOutputV1]',
        'version': 'str'
    }

    attribute_map = {
        'configuration_options': 'configurationOptions',
        'default_max_capsule_duration': 'defaultMaxCapsuleDuration',
        'default_max_interpolation': 'defaultMaxInterpolation',
        'priorities': 'priorities',
        'server_specs': 'serverSpecs',
        'version': 'version'
    }

    def __init__(self, configuration_options=None, default_max_capsule_duration=None, default_max_interpolation=None, priorities=None, server_specs=None, version=None):
        """
        ServerStatusOutputV1 - a model defined in Swagger
        """

        self._configuration_options = None
        self._default_max_capsule_duration = None
        self._default_max_interpolation = None
        self._priorities = None
        self._server_specs = None
        self._version = None

        if configuration_options is not None:
          self.configuration_options = configuration_options
        if default_max_capsule_duration is not None:
          self.default_max_capsule_duration = default_max_capsule_duration
        if default_max_interpolation is not None:
          self.default_max_interpolation = default_max_interpolation
        if priorities is not None:
          self.priorities = priorities
        if server_specs is not None:
          self.server_specs = server_specs
        if version is not None:
          self.version = version

    @property
    def configuration_options(self):
        """
        Gets the configuration_options of this ServerStatusOutputV1.
        A collection of configuration options and their values

        :return: The configuration_options of this ServerStatusOutputV1.
        :rtype: list[ConfigurationOptionOutputSimpleV1]
        """
        return self._configuration_options

    @configuration_options.setter
    def configuration_options(self, configuration_options):
        """
        Sets the configuration_options of this ServerStatusOutputV1.
        A collection of configuration options and their values

        :param configuration_options: The configuration_options of this ServerStatusOutputV1.
        :type: list[ConfigurationOptionOutputSimpleV1]
        """

        self._configuration_options = configuration_options

    @property
    def default_max_capsule_duration(self):
        """
        Gets the default_max_capsule_duration of this ServerStatusOutputV1.
        The scalar value of the default capsule duration

        :return: The default_max_capsule_duration of this ServerStatusOutputV1.
        :rtype: ScalarValueOutputV1
        """
        return self._default_max_capsule_duration

    @default_max_capsule_duration.setter
    def default_max_capsule_duration(self, default_max_capsule_duration):
        """
        Sets the default_max_capsule_duration of this ServerStatusOutputV1.
        The scalar value of the default capsule duration

        :param default_max_capsule_duration: The default_max_capsule_duration of this ServerStatusOutputV1.
        :type: ScalarValueOutputV1
        """

        self._default_max_capsule_duration = default_max_capsule_duration

    @property
    def default_max_interpolation(self):
        """
        Gets the default_max_interpolation of this ServerStatusOutputV1.
        The scalar value of the default maximum interpolation

        :return: The default_max_interpolation of this ServerStatusOutputV1.
        :rtype: ScalarValueOutputV1
        """
        return self._default_max_interpolation

    @default_max_interpolation.setter
    def default_max_interpolation(self, default_max_interpolation):
        """
        Sets the default_max_interpolation of this ServerStatusOutputV1.
        The scalar value of the default maximum interpolation

        :param default_max_interpolation: The default_max_interpolation of this ServerStatusOutputV1.
        :type: ScalarValueOutputV1
        """

        self._default_max_interpolation = default_max_interpolation

    @property
    def priorities(self):
        """
        Gets the priorities of this ServerStatusOutputV1.
        The priorities for metrics, sorted descending by level

        :return: The priorities of this ServerStatusOutputV1.
        :rtype: list[PriorityV1]
        """
        return self._priorities

    @priorities.setter
    def priorities(self, priorities):
        """
        Sets the priorities of this ServerStatusOutputV1.
        The priorities for metrics, sorted descending by level

        :param priorities: The priorities of this ServerStatusOutputV1.
        :type: list[PriorityV1]
        """

        self._priorities = priorities

    @property
    def server_specs(self):
        """
        Gets the server_specs of this ServerStatusOutputV1.
        Information about the specs of the server

        :return: The server_specs of this ServerStatusOutputV1.
        :rtype: list[ServerSpecOutputV1]
        """
        return self._server_specs

    @server_specs.setter
    def server_specs(self, server_specs):
        """
        Sets the server_specs of this ServerStatusOutputV1.
        Information about the specs of the server

        :param server_specs: The server_specs of this ServerStatusOutputV1.
        :type: list[ServerSpecOutputV1]
        """

        self._server_specs = server_specs

    @property
    def version(self):
        """
        Gets the version of this ServerStatusOutputV1.
        The version of Seeq running on the server

        :return: The version of this ServerStatusOutputV1.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ServerStatusOutputV1.
        The version of Seeq running on the server

        :param version: The version of this ServerStatusOutputV1.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, ServerStatusOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
