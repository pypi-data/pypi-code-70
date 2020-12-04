# coding: utf-8

"""
    Contacts

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.contacts.configuration import Configuration


class SimplePublicObject(object):
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
        'id': 'str',
        'properties': 'dict(str, str)',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'associations': 'dict(str, CollectionResponseAssociatedId)',
        'archived': 'bool',
        'archived_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'properties': 'properties',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'associations': 'associations',
        'archived': 'archived',
        'archived_at': 'archivedAt'
    }

    def __init__(self, id=None, properties=None, created_at=None, updated_at=None, associations=None, archived=None, archived_at=None, local_vars_configuration=None):  # noqa: E501
        """SimplePublicObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._properties = None
        self._created_at = None
        self._updated_at = None
        self._associations = None
        self._archived = None
        self._archived_at = None
        self.discriminator = None

        self.id = id
        self.properties = properties
        self.created_at = created_at
        self.updated_at = updated_at
        if associations is not None:
            self.associations = associations
        if archived is not None:
            self.archived = archived
        if archived_at is not None:
            self.archived_at = archived_at

    @property
    def id(self):
        """Gets the id of this SimplePublicObject.  # noqa: E501


        :return: The id of this SimplePublicObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimplePublicObject.


        :param id: The id of this SimplePublicObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this SimplePublicObject.  # noqa: E501


        :return: The properties of this SimplePublicObject.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SimplePublicObject.


        :param properties: The properties of this SimplePublicObject.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def created_at(self):
        """Gets the created_at of this SimplePublicObject.  # noqa: E501


        :return: The created_at of this SimplePublicObject.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SimplePublicObject.


        :param created_at: The created_at of this SimplePublicObject.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SimplePublicObject.  # noqa: E501


        :return: The updated_at of this SimplePublicObject.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SimplePublicObject.


        :param updated_at: The updated_at of this SimplePublicObject.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def associations(self):
        """Gets the associations of this SimplePublicObject.  # noqa: E501


        :return: The associations of this SimplePublicObject.  # noqa: E501
        :rtype: dict(str, CollectionResponseAssociatedId)
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this SimplePublicObject.


        :param associations: The associations of this SimplePublicObject.  # noqa: E501
        :type: dict(str, CollectionResponseAssociatedId)
        """

        self._associations = associations

    @property
    def archived(self):
        """Gets the archived of this SimplePublicObject.  # noqa: E501


        :return: The archived of this SimplePublicObject.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SimplePublicObject.


        :param archived: The archived of this SimplePublicObject.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def archived_at(self):
        """Gets the archived_at of this SimplePublicObject.  # noqa: E501


        :return: The archived_at of this SimplePublicObject.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this SimplePublicObject.


        :param archived_at: The archived_at of this SimplePublicObject.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

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
        if not isinstance(other, SimplePublicObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimplePublicObject):
            return True

        return self.to_dict() != other.to_dict()
