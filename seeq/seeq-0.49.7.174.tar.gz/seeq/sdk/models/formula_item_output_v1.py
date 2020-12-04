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


class FormulaItemOutputV1(object):
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
        'additional_properties': 'list[ScalarPropertyV1]',
        'archived': 'bool',
        'data_id': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'formula': 'str',
        'href': 'str',
        'id': 'str',
        'name': 'str',
        'parameters': 'list[FormulaParameterOutputV1]',
        'permissions_from_datasource': 'bool',
        'scoped_to': 'str',
        'security_string': 'str',
        'source_security_string': 'str',
        'status_message': 'str',
        'type': 'str',
        'upgrade_details': 'FormulaUpgradeOutputV1'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'archived': 'archived',
        'data_id': 'dataId',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'formula': 'formula',
        'href': 'href',
        'id': 'id',
        'name': 'name',
        'parameters': 'parameters',
        'permissions_from_datasource': 'permissionsFromDatasource',
        'scoped_to': 'scopedTo',
        'security_string': 'securityString',
        'source_security_string': 'sourceSecurityString',
        'status_message': 'statusMessage',
        'type': 'type',
        'upgrade_details': 'upgradeDetails'
    }

    def __init__(self, additional_properties=None, archived=False, data_id=None, datasource_class=None, datasource_id=None, description=None, effective_permissions=None, formula=None, href=None, id=None, name=None, parameters=None, permissions_from_datasource=False, scoped_to=None, security_string=None, source_security_string=None, status_message=None, type=None, upgrade_details=None):
        """
        FormulaItemOutputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._archived = None
        self._data_id = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._effective_permissions = None
        self._formula = None
        self._href = None
        self._id = None
        self._name = None
        self._parameters = None
        self._permissions_from_datasource = None
        self._scoped_to = None
        self._security_string = None
        self._source_security_string = None
        self._status_message = None
        self._type = None
        self._upgrade_details = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if archived is not None:
          self.archived = archived
        if data_id is not None:
          self.data_id = data_id
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if formula is not None:
          self.formula = formula
        if href is not None:
          self.href = href
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if parameters is not None:
          self.parameters = parameters
        if permissions_from_datasource is not None:
          self.permissions_from_datasource = permissions_from_datasource
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if security_string is not None:
          self.security_string = security_string
        if source_security_string is not None:
          self.source_security_string = source_security_string
        if status_message is not None:
          self.status_message = status_message
        if type is not None:
          self.type = type
        if upgrade_details is not None:
          self.upgrade_details = upgrade_details

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this FormulaItemOutputV1.
        Additional properties of the item

        :return: The additional_properties of this FormulaItemOutputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this FormulaItemOutputV1.
        Additional properties of the item

        :param additional_properties: The additional_properties of this FormulaItemOutputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def archived(self):
        """
        Gets the archived of this FormulaItemOutputV1.

        :return: The archived of this FormulaItemOutputV1.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this FormulaItemOutputV1.

        :param archived: The archived of this FormulaItemOutputV1.
        :type: bool
        """

        self._archived = archived

    @property
    def data_id(self):
        """
        Gets the data_id of this FormulaItemOutputV1.
        The data ID of this asset. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this FormulaItemOutputV1.
        The data ID of this asset. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this FormulaItemOutputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this FormulaItemOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :return: The datasource_class of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this FormulaItemOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :param datasource_class: The datasource_class of this FormulaItemOutputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this FormulaItemOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :return: The datasource_id of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this FormulaItemOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :param datasource_id: The datasource_id of this FormulaItemOutputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this FormulaItemOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FormulaItemOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this FormulaItemOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this FormulaItemOutputV1.
        The permissions the current user has to the item.

        :return: The effective_permissions of this FormulaItemOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this FormulaItemOutputV1.
        The permissions the current user has to the item.

        :param effective_permissions: The effective_permissions of this FormulaItemOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def formula(self):
        """
        Gets the formula of this FormulaItemOutputV1.
        The formula for the calculated item

        :return: The formula of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this FormulaItemOutputV1.
        The formula for the calculated item

        :param formula: The formula of this FormulaItemOutputV1.
        :type: str
        """

        self._formula = formula

    @property
    def href(self):
        """
        Gets the href of this FormulaItemOutputV1.
        The href that can be used to interact with the item

        :return: The href of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this FormulaItemOutputV1.
        The href that can be used to interact with the item

        :param href: The href of this FormulaItemOutputV1.
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def id(self):
        """
        Gets the id of this FormulaItemOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FormulaItemOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this FormulaItemOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FormulaItemOutputV1.
        The human readable name

        :return: The name of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FormulaItemOutputV1.
        The human readable name

        :param name: The name of this FormulaItemOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parameters(self):
        """
        Gets the parameters of this FormulaItemOutputV1.
        Parameters that are used in the context of executing the formula

        :return: The parameters of this FormulaItemOutputV1.
        :rtype: list[FormulaParameterOutputV1]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this FormulaItemOutputV1.
        Parameters that are used in the context of executing the formula

        :param parameters: The parameters of this FormulaItemOutputV1.
        :type: list[FormulaParameterOutputV1]
        """

        self._parameters = parameters

    @property
    def permissions_from_datasource(self):
        """
        Gets the permissions_from_datasource of this FormulaItemOutputV1.
        True if permissions are managed by the datasource, false if they are managed in Seeq

        :return: The permissions_from_datasource of this FormulaItemOutputV1.
        :rtype: bool
        """
        return self._permissions_from_datasource

    @permissions_from_datasource.setter
    def permissions_from_datasource(self, permissions_from_datasource):
        """
        Sets the permissions_from_datasource of this FormulaItemOutputV1.
        True if permissions are managed by the datasource, false if they are managed in Seeq

        :param permissions_from_datasource: The permissions_from_datasource of this FormulaItemOutputV1.
        :type: bool
        """

        self._permissions_from_datasource = permissions_from_datasource

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this FormulaItemOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :return: The scoped_to of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this FormulaItemOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :param scoped_to: The scoped_to of this FormulaItemOutputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def security_string(self):
        """
        Gets the security_string of this FormulaItemOutputV1.
        Security string in Seeq format provided by datasource

        :return: The security_string of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._security_string

    @security_string.setter
    def security_string(self, security_string):
        """
        Sets the security_string of this FormulaItemOutputV1.
        Security string in Seeq format provided by datasource

        :param security_string: The security_string of this FormulaItemOutputV1.
        :type: str
        """

        self._security_string = security_string

    @property
    def source_security_string(self):
        """
        Gets the source_security_string of this FormulaItemOutputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :return: The source_security_string of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._source_security_string

    @source_security_string.setter
    def source_security_string(self, source_security_string):
        """
        Sets the source_security_string of this FormulaItemOutputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :param source_security_string: The source_security_string of this FormulaItemOutputV1.
        :type: str
        """

        self._source_security_string = source_security_string

    @property
    def status_message(self):
        """
        Gets the status_message of this FormulaItemOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this FormulaItemOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this FormulaItemOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def type(self):
        """
        Gets the type of this FormulaItemOutputV1.
        The type of the item

        :return: The type of this FormulaItemOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FormulaItemOutputV1.
        The type of the item

        :param type: The type of this FormulaItemOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def upgrade_details(self):
        """
        Gets the upgrade_details of this FormulaItemOutputV1.
        Contains upgrade information if the formula contains legacy syntax that was automatically updated

        :return: The upgrade_details of this FormulaItemOutputV1.
        :rtype: FormulaUpgradeOutputV1
        """
        return self._upgrade_details

    @upgrade_details.setter
    def upgrade_details(self, upgrade_details):
        """
        Sets the upgrade_details of this FormulaItemOutputV1.
        Contains upgrade information if the formula contains legacy syntax that was automatically updated

        :param upgrade_details: The upgrade_details of this FormulaItemOutputV1.
        :type: FormulaUpgradeOutputV1
        """

        self._upgrade_details = upgrade_details

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
        if not isinstance(other, FormulaItemOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
