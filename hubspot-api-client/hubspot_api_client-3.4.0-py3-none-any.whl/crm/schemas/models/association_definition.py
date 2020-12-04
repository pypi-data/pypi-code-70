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


class AssociationDefinition(object):
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
        'from_object_type_id': 'str',
        'to_object_type_id': 'str',
        'name': 'str',
        'cardinality': 'str',
        'inverse_cardinality': 'str',
        'id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'from_object_type_id': 'fromObjectTypeId',
        'to_object_type_id': 'toObjectTypeId',
        'name': 'name',
        'cardinality': 'cardinality',
        'inverse_cardinality': 'inverseCardinality',
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, from_object_type_id=None, to_object_type_id=None, name=None, cardinality=None, inverse_cardinality=None, id=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """AssociationDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._from_object_type_id = None
        self._to_object_type_id = None
        self._name = None
        self._cardinality = None
        self._inverse_cardinality = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.from_object_type_id = from_object_type_id
        self.to_object_type_id = to_object_type_id
        if name is not None:
            self.name = name
        self.cardinality = cardinality
        self.inverse_cardinality = inverse_cardinality
        self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def from_object_type_id(self):
        """Gets the from_object_type_id of this AssociationDefinition.  # noqa: E501

        ID of the primary object type to link from.  # noqa: E501

        :return: The from_object_type_id of this AssociationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._from_object_type_id

    @from_object_type_id.setter
    def from_object_type_id(self, from_object_type_id):
        """Sets the from_object_type_id of this AssociationDefinition.

        ID of the primary object type to link from.  # noqa: E501

        :param from_object_type_id: The from_object_type_id of this AssociationDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and from_object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `from_object_type_id`, must not be `None`")  # noqa: E501

        self._from_object_type_id = from_object_type_id

    @property
    def to_object_type_id(self):
        """Gets the to_object_type_id of this AssociationDefinition.  # noqa: E501

        ID of the target object type ID to link to.  # noqa: E501

        :return: The to_object_type_id of this AssociationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._to_object_type_id

    @to_object_type_id.setter
    def to_object_type_id(self, to_object_type_id):
        """Sets the to_object_type_id of this AssociationDefinition.

        ID of the target object type ID to link to.  # noqa: E501

        :param to_object_type_id: The to_object_type_id of this AssociationDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to_object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `to_object_type_id`, must not be `None`")  # noqa: E501

        self._to_object_type_id = to_object_type_id

    @property
    def name(self):
        """Gets the name of this AssociationDefinition.  # noqa: E501

        A unique name for this association.  # noqa: E501

        :return: The name of this AssociationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssociationDefinition.

        A unique name for this association.  # noqa: E501

        :param name: The name of this AssociationDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cardinality(self):
        """Gets the cardinality of this AssociationDefinition.  # noqa: E501


        :return: The cardinality of this AssociationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """Sets the cardinality of this AssociationDefinition.


        :param cardinality: The cardinality of this AssociationDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cardinality is None:  # noqa: E501
            raise ValueError("Invalid value for `cardinality`, must not be `None`")  # noqa: E501
        allowed_values = ["ONE_TO_ONE", "ONE_TO_MANY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cardinality not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cardinality` ({0}), must be one of {1}"  # noqa: E501
                .format(cardinality, allowed_values)
            )

        self._cardinality = cardinality

    @property
    def inverse_cardinality(self):
        """Gets the inverse_cardinality of this AssociationDefinition.  # noqa: E501


        :return: The inverse_cardinality of this AssociationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._inverse_cardinality

    @inverse_cardinality.setter
    def inverse_cardinality(self, inverse_cardinality):
        """Sets the inverse_cardinality of this AssociationDefinition.


        :param inverse_cardinality: The inverse_cardinality of this AssociationDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inverse_cardinality is None:  # noqa: E501
            raise ValueError("Invalid value for `inverse_cardinality`, must not be `None`")  # noqa: E501
        allowed_values = ["ONE_TO_ONE", "ONE_TO_MANY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and inverse_cardinality not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `inverse_cardinality` ({0}), must be one of {1}"  # noqa: E501
                .format(inverse_cardinality, allowed_values)
            )

        self._inverse_cardinality = inverse_cardinality

    @property
    def id(self):
        """Gets the id of this AssociationDefinition.  # noqa: E501

        A unique ID for this association.  # noqa: E501

        :return: The id of this AssociationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssociationDefinition.

        A unique ID for this association.  # noqa: E501

        :param id: The id of this AssociationDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this AssociationDefinition.  # noqa: E501

        When the association was defined.  # noqa: E501

        :return: The created_at of this AssociationDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AssociationDefinition.

        When the association was defined.  # noqa: E501

        :param created_at: The created_at of this AssociationDefinition.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AssociationDefinition.  # noqa: E501

        When the association was last updated.  # noqa: E501

        :return: The updated_at of this AssociationDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AssociationDefinition.

        When the association was last updated.  # noqa: E501

        :param updated_at: The updated_at of this AssociationDefinition.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, AssociationDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssociationDefinition):
            return True

        return self.to_dict() != other.to_dict()
