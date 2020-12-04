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


class ObjectSchema(object):
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
        'id': 'str',
        'fully_qualified_name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'object_type_id': 'str',
        'properties': 'list[ModelProperty]',
        'associations': 'list[AssociationDefinition]',
        'name': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'required_properties': 'requiredProperties',
        'searchable_properties': 'searchableProperties',
        'primary_display_property': 'primaryDisplayProperty',
        'secondary_display_properties': 'secondaryDisplayProperties',
        'id': 'id',
        'fully_qualified_name': 'fullyQualifiedName',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'object_type_id': 'objectTypeId',
        'properties': 'properties',
        'associations': 'associations',
        'name': 'name'
    }

    def __init__(self, labels=None, required_properties=None, searchable_properties=None, primary_display_property=None, secondary_display_properties=None, id=None, fully_qualified_name=None, created_at=None, updated_at=None, object_type_id=None, properties=None, associations=None, name=None, local_vars_configuration=None):  # noqa: E501
        """ObjectSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._labels = None
        self._required_properties = None
        self._searchable_properties = None
        self._primary_display_property = None
        self._secondary_display_properties = None
        self._id = None
        self._fully_qualified_name = None
        self._created_at = None
        self._updated_at = None
        self._object_type_id = None
        self._properties = None
        self._associations = None
        self._name = None
        self.discriminator = None

        self.labels = labels
        self.required_properties = required_properties
        self.searchable_properties = searchable_properties
        if primary_display_property is not None:
            self.primary_display_property = primary_display_property
        self.secondary_display_properties = secondary_display_properties
        self.id = id
        self.fully_qualified_name = fully_qualified_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.object_type_id = object_type_id
        self.properties = properties
        self.associations = associations
        self.name = name

    @property
    def labels(self):
        """Gets the labels of this ObjectSchema.  # noqa: E501


        :return: The labels of this ObjectSchema.  # noqa: E501
        :rtype: ObjectTypeDefinitionLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ObjectSchema.


        :param labels: The labels of this ObjectSchema.  # noqa: E501
        :type: ObjectTypeDefinitionLabels
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def required_properties(self):
        """Gets the required_properties of this ObjectSchema.  # noqa: E501

        The names of properties that should be **required** when creating an object of this type.  # noqa: E501

        :return: The required_properties of this ObjectSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_properties

    @required_properties.setter
    def required_properties(self, required_properties):
        """Sets the required_properties of this ObjectSchema.

        The names of properties that should be **required** when creating an object of this type.  # noqa: E501

        :param required_properties: The required_properties of this ObjectSchema.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and required_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `required_properties`, must not be `None`")  # noqa: E501

        self._required_properties = required_properties

    @property
    def searchable_properties(self):
        """Gets the searchable_properties of this ObjectSchema.  # noqa: E501

        Names of properties that will be indexed for this object type in by HubSpot's product search.  # noqa: E501

        :return: The searchable_properties of this ObjectSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._searchable_properties

    @searchable_properties.setter
    def searchable_properties(self, searchable_properties):
        """Sets the searchable_properties of this ObjectSchema.

        Names of properties that will be indexed for this object type in by HubSpot's product search.  # noqa: E501

        :param searchable_properties: The searchable_properties of this ObjectSchema.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and searchable_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `searchable_properties`, must not be `None`")  # noqa: E501

        self._searchable_properties = searchable_properties

    @property
    def primary_display_property(self):
        """Gets the primary_display_property of this ObjectSchema.  # noqa: E501

        The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.  # noqa: E501

        :return: The primary_display_property of this ObjectSchema.  # noqa: E501
        :rtype: str
        """
        return self._primary_display_property

    @primary_display_property.setter
    def primary_display_property(self, primary_display_property):
        """Sets the primary_display_property of this ObjectSchema.

        The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.  # noqa: E501

        :param primary_display_property: The primary_display_property of this ObjectSchema.  # noqa: E501
        :type: str
        """

        self._primary_display_property = primary_display_property

    @property
    def secondary_display_properties(self):
        """Gets the secondary_display_properties of this ObjectSchema.  # noqa: E501

        The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.  # noqa: E501

        :return: The secondary_display_properties of this ObjectSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._secondary_display_properties

    @secondary_display_properties.setter
    def secondary_display_properties(self, secondary_display_properties):
        """Sets the secondary_display_properties of this ObjectSchema.

        The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.  # noqa: E501

        :param secondary_display_properties: The secondary_display_properties of this ObjectSchema.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and secondary_display_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `secondary_display_properties`, must not be `None`")  # noqa: E501

        self._secondary_display_properties = secondary_display_properties

    @property
    def id(self):
        """Gets the id of this ObjectSchema.  # noqa: E501

        A unique ID for this schema's object type. Will be defined as {meta-type}-{unique ID}.  # noqa: E501

        :return: The id of this ObjectSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectSchema.

        A unique ID for this schema's object type. Will be defined as {meta-type}-{unique ID}.  # noqa: E501

        :param id: The id of this ObjectSchema.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def fully_qualified_name(self):
        """Gets the fully_qualified_name of this ObjectSchema.  # noqa: E501

        An assigned unique ID for the object, including portal ID and object name.  # noqa: E501

        :return: The fully_qualified_name of this ObjectSchema.  # noqa: E501
        :rtype: str
        """
        return self._fully_qualified_name

    @fully_qualified_name.setter
    def fully_qualified_name(self, fully_qualified_name):
        """Sets the fully_qualified_name of this ObjectSchema.

        An assigned unique ID for the object, including portal ID and object name.  # noqa: E501

        :param fully_qualified_name: The fully_qualified_name of this ObjectSchema.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and fully_qualified_name is None:  # noqa: E501
            raise ValueError("Invalid value for `fully_qualified_name`, must not be `None`")  # noqa: E501

        self._fully_qualified_name = fully_qualified_name

    @property
    def created_at(self):
        """Gets the created_at of this ObjectSchema.  # noqa: E501

        When the object schema was created.  # noqa: E501

        :return: The created_at of this ObjectSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ObjectSchema.

        When the object schema was created.  # noqa: E501

        :param created_at: The created_at of this ObjectSchema.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ObjectSchema.  # noqa: E501

        When the object schema was last updated.  # noqa: E501

        :return: The updated_at of this ObjectSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ObjectSchema.

        When the object schema was last updated.  # noqa: E501

        :param updated_at: The updated_at of this ObjectSchema.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def object_type_id(self):
        """Gets the object_type_id of this ObjectSchema.  # noqa: E501


        :return: The object_type_id of this ObjectSchema.  # noqa: E501
        :rtype: str
        """
        return self._object_type_id

    @object_type_id.setter
    def object_type_id(self, object_type_id):
        """Sets the object_type_id of this ObjectSchema.


        :param object_type_id: The object_type_id of this ObjectSchema.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_type_id`, must not be `None`")  # noqa: E501

        self._object_type_id = object_type_id

    @property
    def properties(self):
        """Gets the properties of this ObjectSchema.  # noqa: E501

        Properties defined for this object type.  # noqa: E501

        :return: The properties of this ObjectSchema.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ObjectSchema.

        Properties defined for this object type.  # noqa: E501

        :param properties: The properties of this ObjectSchema.  # noqa: E501
        :type: list[ModelProperty]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def associations(self):
        """Gets the associations of this ObjectSchema.  # noqa: E501

        Associations defined for a given object type.  # noqa: E501

        :return: The associations of this ObjectSchema.  # noqa: E501
        :rtype: list[AssociationDefinition]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this ObjectSchema.

        Associations defined for a given object type.  # noqa: E501

        :param associations: The associations of this ObjectSchema.  # noqa: E501
        :type: list[AssociationDefinition]
        """
        if self.local_vars_configuration.client_side_validation and associations is None:  # noqa: E501
            raise ValueError("Invalid value for `associations`, must not be `None`")  # noqa: E501

        self._associations = associations

    @property
    def name(self):
        """Gets the name of this ObjectSchema.  # noqa: E501

        A unique name for the schema's object type.  # noqa: E501

        :return: The name of this ObjectSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectSchema.

        A unique name for the schema's object type.  # noqa: E501

        :param name: The name of this ObjectSchema.  # noqa: E501
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
        if not isinstance(other, ObjectSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectSchema):
            return True

        return self.to_dict() != other.to_dict()
