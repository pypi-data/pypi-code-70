# coding: utf-8

"""
    Schemas

    The CRM uses schemas to define how custom objects should store and represent information in the HubSpot CRM. Schemas define details about an object's type, properties, and associations. The schema can be uniquely identified by its **object type ID**.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.schemas.configuration import Configuration


class ObjectSchemaEgg(object):
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
        'labels': 'ObjectTypeDefinitionLabels',
        'required_properties': 'list[str]',
        'searchable_properties': 'list[str]',
        'primary_display_property': 'str',
        'secondary_display_properties': 'list[str]',
        'properties': 'list[ObjectTypePropertyCreate]',
        'associated_objects': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'required_properties': 'requiredProperties',
        'searchable_properties': 'searchableProperties',
        'primary_display_property': 'primaryDisplayProperty',
        'secondary_display_properties': 'secondaryDisplayProperties',
        'properties': 'properties',
        'associated_objects': 'associatedObjects',
        'name': 'name'
    }

    def __init__(self, labels=None, required_properties=None, searchable_properties=None, primary_display_property=None, secondary_display_properties=None, properties=None, associated_objects=None, name=None, local_vars_configuration=None):  # noqa: E501
        """ObjectSchemaEgg - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._labels = None
        self._required_properties = None
        self._searchable_properties = None
        self._primary_display_property = None
        self._secondary_display_properties = None
        self._properties = None
        self._associated_objects = None
        self._name = None
        self.discriminator = None

        self.labels = labels
        self.required_properties = required_properties
        self.searchable_properties = searchable_properties
        if primary_display_property is not None:
            self.primary_display_property = primary_display_property
        self.secondary_display_properties = secondary_display_properties
        self.properties = properties
        self.associated_objects = associated_objects
        self.name = name

    @property
    def labels(self):
        """Gets the labels of this ObjectSchemaEgg.  # noqa: E501


        :return: The labels of this ObjectSchemaEgg.  # noqa: E501
        :rtype: ObjectTypeDefinitionLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ObjectSchemaEgg.


        :param labels: The labels of this ObjectSchemaEgg.  # noqa: E501
        :type: ObjectTypeDefinitionLabels
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def required_properties(self):
        """Gets the required_properties of this ObjectSchemaEgg.  # noqa: E501

        The names of properties that should be **required** when creating an object of this type.  # noqa: E501

        :return: The required_properties of this ObjectSchemaEgg.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_properties

    @required_properties.setter
    def required_properties(self, required_properties):
        """Sets the required_properties of this ObjectSchemaEgg.

        The names of properties that should be **required** when creating an object of this type.  # noqa: E501

        :param required_properties: The required_properties of this ObjectSchemaEgg.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and required_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `required_properties`, must not be `None`")  # noqa: E501

        self._required_properties = required_properties

    @property
    def searchable_properties(self):
        """Gets the searchable_properties of this ObjectSchemaEgg.  # noqa: E501

        Names of properties that will be indexed for this object type in by HubSpot's product search.  # noqa: E501

        :return: The searchable_properties of this ObjectSchemaEgg.  # noqa: E501
        :rtype: list[str]
        """
        return self._searchable_properties

    @searchable_properties.setter
    def searchable_properties(self, searchable_properties):
        """Sets the searchable_properties of this ObjectSchemaEgg.

        Names of properties that will be indexed for this object type in by HubSpot's product search.  # noqa: E501

        :param searchable_properties: The searchable_properties of this ObjectSchemaEgg.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and searchable_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `searchable_properties`, must not be `None`")  # noqa: E501

        self._searchable_properties = searchable_properties

    @property
    def primary_display_property(self):
        """Gets the primary_display_property of this ObjectSchemaEgg.  # noqa: E501

        The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.  # noqa: E501

        :return: The primary_display_property of this ObjectSchemaEgg.  # noqa: E501
        :rtype: str
        """
        return self._primary_display_property

    @primary_display_property.setter
    def primary_display_property(self, primary_display_property):
        """Sets the primary_display_property of this ObjectSchemaEgg.

        The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.  # noqa: E501

        :param primary_display_property: The primary_display_property of this ObjectSchemaEgg.  # noqa: E501
        :type: str
        """

        self._primary_display_property = primary_display_property

    @property
    def secondary_display_properties(self):
        """Gets the secondary_display_properties of this ObjectSchemaEgg.  # noqa: E501

        The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.  # noqa: E501

        :return: The secondary_display_properties of this ObjectSchemaEgg.  # noqa: E501
        :rtype: list[str]
        """
        return self._secondary_display_properties

    @secondary_display_properties.setter
    def secondary_display_properties(self, secondary_display_properties):
        """Sets the secondary_display_properties of this ObjectSchemaEgg.

        The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.  # noqa: E501

        :param secondary_display_properties: The secondary_display_properties of this ObjectSchemaEgg.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and secondary_display_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `secondary_display_properties`, must not be `None`")  # noqa: E501

        self._secondary_display_properties = secondary_display_properties

    @property
    def properties(self):
        """Gets the properties of this ObjectSchemaEgg.  # noqa: E501

        Properties defined for this object type.  # noqa: E501

        :return: The properties of this ObjectSchemaEgg.  # noqa: E501
        :rtype: list[ObjectTypePropertyCreate]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ObjectSchemaEgg.

        Properties defined for this object type.  # noqa: E501

        :param properties: The properties of this ObjectSchemaEgg.  # noqa: E501
        :type: list[ObjectTypePropertyCreate]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def associated_objects(self):
        """Gets the associated_objects of this ObjectSchemaEgg.  # noqa: E501

        Associations defined for this object type.  # noqa: E501

        :return: The associated_objects of this ObjectSchemaEgg.  # noqa: E501
        :rtype: list[str]
        """
        return self._associated_objects

    @associated_objects.setter
    def associated_objects(self, associated_objects):
        """Sets the associated_objects of this ObjectSchemaEgg.

        Associations defined for this object type.  # noqa: E501

        :param associated_objects: The associated_objects of this ObjectSchemaEgg.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and associated_objects is None:  # noqa: E501
            raise ValueError("Invalid value for `associated_objects`, must not be `None`")  # noqa: E501

        self._associated_objects = associated_objects

    @property
    def name(self):
        """Gets the name of this ObjectSchemaEgg.  # noqa: E501

        A unique name for this object. For internal use only.  # noqa: E501

        :return: The name of this ObjectSchemaEgg.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectSchemaEgg.

        A unique name for this object. For internal use only.  # noqa: E501

        :param name: The name of this ObjectSchemaEgg.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, ObjectSchemaEgg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectSchemaEgg):
            return True

        return self.to_dict() != other.to_dict()
