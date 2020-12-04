# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 50.3.1-BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConfigurationOptionOutputV1(object):
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
        'advanced': 'bool',
        'allowed_values': 'str',
        'default_dependencies': 'list[str]',
        'default_description': 'str',
        'default_value': 'object',
        'description': 'str',
        'modifiable': 'bool',
        'note': 'str',
        'path': 'str',
        'registration': 'str',
        'registration_description': 'str',
        'units': 'str',
        'value': 'object'
    }

    attribute_map = {
        'advanced': 'advanced',
        'allowed_values': 'allowedValues',
        'default_dependencies': 'defaultDependencies',
        'default_description': 'defaultDescription',
        'default_value': 'defaultValue',
        'description': 'description',
        'modifiable': 'modifiable',
        'note': 'note',
        'path': 'path',
        'registration': 'registration',
        'registration_description': 'registrationDescription',
        'units': 'units',
        'value': 'value'
    }

    def __init__(self, advanced=False, allowed_values=None, default_dependencies=None, default_description=None, default_value=None, description=None, modifiable=False, note=None, path=None, registration=None, registration_description=None, units=None, value=None):
        """
        ConfigurationOptionOutputV1 - a model defined in Swagger
        """

        self._advanced = None
        self._allowed_values = None
        self._default_dependencies = None
        self._default_description = None
        self._default_value = None
        self._description = None
        self._modifiable = None
        self._note = None
        self._path = None
        self._registration = None
        self._registration_description = None
        self._units = None
        self._value = None

        if advanced is not None:
          self.advanced = advanced
        if allowed_values is not None:
          self.allowed_values = allowed_values
        if default_dependencies is not None:
          self.default_dependencies = default_dependencies
        if default_description is not None:
          self.default_description = default_description
        if default_value is not None:
          self.default_value = default_value
        if description is not None:
          self.description = description
        if modifiable is not None:
          self.modifiable = modifiable
        if note is not None:
          self.note = note
        if path is not None:
          self.path = path
        if registration is not None:
          self.registration = registration
        if registration_description is not None:
          self.registration_description = registration_description
        if units is not None:
          self.units = units
        if value is not None:
          self.value = value

    @property
    def advanced(self):
        """
        Gets the advanced of this ConfigurationOptionOutputV1.
        True if this configuration option can have ramifications for performance and stability. Consider consulting with Seeq Support before changing.

        :return: The advanced of this ConfigurationOptionOutputV1.
        :rtype: bool
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """
        Sets the advanced of this ConfigurationOptionOutputV1.
        True if this configuration option can have ramifications for performance and stability. Consider consulting with Seeq Support before changing.

        :param advanced: The advanced of this ConfigurationOptionOutputV1.
        :type: bool
        """
        if advanced is None:
            raise ValueError("Invalid value for `advanced`, must not be `None`")

        self._advanced = advanced

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this ConfigurationOptionOutputV1.
        If present, a plain text description of the allowed values.

        :return: The allowed_values of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this ConfigurationOptionOutputV1.
        If present, a plain text description of the allowed values.

        :param allowed_values: The allowed_values of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._allowed_values = allowed_values

    @property
    def default_dependencies(self):
        """
        Gets the default_dependencies of this ConfigurationOptionOutputV1.
        If present, the list of paths that the default value depend on.

        :return: The default_dependencies of this ConfigurationOptionOutputV1.
        :rtype: list[str]
        """
        return self._default_dependencies

    @default_dependencies.setter
    def default_dependencies(self, default_dependencies):
        """
        Sets the default_dependencies of this ConfigurationOptionOutputV1.
        If present, the list of paths that the default value depend on.

        :param default_dependencies: The default_dependencies of this ConfigurationOptionOutputV1.
        :type: list[str]
        """

        self._default_dependencies = default_dependencies

    @property
    def default_description(self):
        """
        Gets the default_description of this ConfigurationOptionOutputV1.
        If present, any additional, plain text context for the default value.

        :return: The default_description of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._default_description

    @default_description.setter
    def default_description(self, default_description):
        """
        Sets the default_description of this ConfigurationOptionOutputV1.
        If present, any additional, plain text context for the default value.

        :param default_description: The default_description of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._default_description = default_description

    @property
    def default_value(self):
        """
        Gets the default_value of this ConfigurationOptionOutputV1.
        The value that this property would have if the option has not been explicitly set to a value.

        :return: The default_value of this ConfigurationOptionOutputV1.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ConfigurationOptionOutputV1.
        The value that this property would have if the option has not been explicitly set to a value.

        :param default_value: The default_value of this ConfigurationOptionOutputV1.
        :type: object
        """
        if default_value is None:
            raise ValueError("Invalid value for `default_value`, must not be `None`")

        self._default_value = default_value

    @property
    def description(self):
        """
        Gets the description of this ConfigurationOptionOutputV1.
        The plain text description a configuration option's purpose and any important details.

        :return: The description of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigurationOptionOutputV1.
        The plain text description a configuration option's purpose and any important details.

        :param description: The description of this ConfigurationOptionOutputV1.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def modifiable(self):
        """
        Gets the modifiable of this ConfigurationOptionOutputV1.
        True if the configuration option can be set by server administrators.

        :return: The modifiable of this ConfigurationOptionOutputV1.
        :rtype: bool
        """
        return self._modifiable

    @modifiable.setter
    def modifiable(self, modifiable):
        """
        Sets the modifiable of this ConfigurationOptionOutputV1.
        True if the configuration option can be set by server administrators.

        :param modifiable: The modifiable of this ConfigurationOptionOutputV1.
        :type: bool
        """
        if modifiable is None:
            raise ValueError("Invalid value for `modifiable`, must not be `None`")

        self._modifiable = modifiable

    @property
    def note(self):
        """
        Gets the note of this ConfigurationOptionOutputV1.
        A plain text note that can be set by server administrators to provide context on any configuration changes.

        :return: The note of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this ConfigurationOptionOutputV1.
        A plain text note that can be set by server administrators to provide context on any configuration changes.

        :param note: The note of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._note = note

    @property
    def path(self):
        """
        Gets the path of this ConfigurationOptionOutputV1.
        The unique identifier of the configuration option. Slashes in the path imply a hierarchy.

        :return: The path of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ConfigurationOptionOutputV1.
        The unique identifier of the configuration option. Slashes in the path imply a hierarchy.

        :param path: The path of this ConfigurationOptionOutputV1.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def registration(self):
        """
        Gets the registration of this ConfigurationOptionOutputV1.
        If present, a plain text description of when the option will take effect when it is changed.

        :return: The registration of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._registration

    @registration.setter
    def registration(self, registration):
        """
        Sets the registration of this ConfigurationOptionOutputV1.
        If present, a plain text description of when the option will take effect when it is changed.

        :param registration: The registration of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._registration = registration

    @property
    def registration_description(self):
        """
        Gets the registration_description of this ConfigurationOptionOutputV1.
        If present, any additional, plain text context for the registration value.

        :return: The registration_description of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._registration_description

    @registration_description.setter
    def registration_description(self, registration_description):
        """
        Sets the registration_description of this ConfigurationOptionOutputV1.
        If present, any additional, plain text context for the registration value.

        :param registration_description: The registration_description of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._registration_description = registration_description

    @property
    def units(self):
        """
        Gets the units of this ConfigurationOptionOutputV1.
        If present, a freeform plain text description of the units of a value.

        :return: The units of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this ConfigurationOptionOutputV1.
        If present, a freeform plain text description of the units of a value.

        :param units: The units of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._units = units

    @property
    def value(self):
        """
        Gets the value of this ConfigurationOptionOutputV1.
        The value of the configuration option. Values can be booleans, strings, or numbers.This value can be set changed if the option is modifiable. An absent value indicates that the option has not been configured.

        :return: The value of this ConfigurationOptionOutputV1.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ConfigurationOptionOutputV1.
        The value of the configuration option. Values can be booleans, strings, or numbers.This value can be set changed if the option is modifiable. An absent value indicates that the option has not been configured.

        :param value: The value of this ConfigurationOptionOutputV1.
        :type: object
        """

        self._value = value

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
        if not isinstance(other, ConfigurationOptionOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
