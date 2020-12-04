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


class ConditionInputV1(object):
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
        'data_id': 'str',
        'data_version_check': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'formula': 'str',
        'host_id': 'str',
        'maximum_duration': 'str',
        'name': 'str',
        'parameters': 'list[str]',
        'properties': 'list[ScalarPropertyV1]',
        'scoped_to': 'str',
        'security_string': 'str',
        'source_security_string': 'str',
        'sync_token': 'str',
        'unit_of_measure': 'str'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'data_id': 'dataId',
        'data_version_check': 'dataVersionCheck',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'formula': 'formula',
        'host_id': 'hostId',
        'maximum_duration': 'maximumDuration',
        'name': 'name',
        'parameters': 'parameters',
        'properties': 'properties',
        'scoped_to': 'scopedTo',
        'security_string': 'securityString',
        'source_security_string': 'sourceSecurityString',
        'sync_token': 'syncToken',
        'unit_of_measure': 'unitOfMeasure'
    }

    def __init__(self, additional_properties=None, data_id=None, data_version_check=None, datasource_class=None, datasource_id=None, description=None, formula=None, host_id=None, maximum_duration=None, name=None, parameters=None, properties=None, scoped_to=None, security_string=None, source_security_string=None, sync_token=None, unit_of_measure=None):
        """
        ConditionInputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._data_id = None
        self._data_version_check = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._formula = None
        self._host_id = None
        self._maximum_duration = None
        self._name = None
        self._parameters = None
        self._properties = None
        self._scoped_to = None
        self._security_string = None
        self._source_security_string = None
        self._sync_token = None
        self._unit_of_measure = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if data_id is not None:
          self.data_id = data_id
        if data_version_check is not None:
          self.data_version_check = data_version_check
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if formula is not None:
          self.formula = formula
        if host_id is not None:
          self.host_id = host_id
        if maximum_duration is not None:
          self.maximum_duration = maximum_duration
        if name is not None:
          self.name = name
        if parameters is not None:
          self.parameters = parameters
        if properties is not None:
          self.properties = properties
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if security_string is not None:
          self.security_string = security_string
        if source_security_string is not None:
          self.source_security_string = source_security_string
        if sync_token is not None:
          self.sync_token = sync_token
        if unit_of_measure is not None:
          self.unit_of_measure = unit_of_measure

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ConditionInputV1.
        Additional properties to set on this item. A property consists of a name, a value, and a unit of measure.

        :return: The additional_properties of this ConditionInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ConditionInputV1.
        Additional properties to set on this item. A property consists of a name, a value, and a unit of measure.

        :param additional_properties: The additional_properties of this ConditionInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def data_id(self):
        """
        Gets the data_id of this ConditionInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this ConditionInputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this ConditionInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this ConditionInputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def data_version_check(self):
        """
        Gets the data_version_check of this ConditionInputV1.
        The data version check string. When updating an existing series, if the data version check string is unchanged, then the update will be skipped.

        :return: The data_version_check of this ConditionInputV1.
        :rtype: str
        """
        return self._data_version_check

    @data_version_check.setter
    def data_version_check(self, data_version_check):
        """
        Sets the data_version_check of this ConditionInputV1.
        The data version check string. When updating an existing series, if the data version check string is unchanged, then the update will be skipped.

        :param data_version_check: The data_version_check of this ConditionInputV1.
        :type: str
        """

        self._data_version_check = data_version_check

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this ConditionInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_class of this ConditionInputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this ConditionInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_class: The datasource_class of this ConditionInputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this ConditionInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_id of this ConditionInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this ConditionInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_id: The datasource_id of this ConditionInputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this ConditionInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :return: The description of this ConditionInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConditionInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :param description: The description of this ConditionInputV1.
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """
        Gets the formula of this ConditionInputV1.
        Information about the formula used to create a calculated item

        :return: The formula of this ConditionInputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this ConditionInputV1.
        Information about the formula used to create a calculated item

        :param formula: The formula of this ConditionInputV1.
        :type: str
        """

        self._formula = formula

    @property
    def host_id(self):
        """
        Gets the host_id of this ConditionInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :return: The host_id of this ConditionInputV1.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this ConditionInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :param host_id: The host_id of this ConditionInputV1.
        :type: str
        """

        self._host_id = host_id

    @property
    def maximum_duration(self):
        """
        Gets the maximum_duration of this ConditionInputV1.
        The maximum duration of capsules in this series. Required for stored conditions.

        :return: The maximum_duration of this ConditionInputV1.
        :rtype: str
        """
        return self._maximum_duration

    @maximum_duration.setter
    def maximum_duration(self, maximum_duration):
        """
        Sets the maximum_duration of this ConditionInputV1.
        The maximum duration of capsules in this series. Required for stored conditions.

        :param maximum_duration: The maximum_duration of this ConditionInputV1.
        :type: str
        """
        if maximum_duration is None:
            raise ValueError("Invalid value for `maximum_duration`, must not be `None`")

        self._maximum_duration = maximum_duration

    @property
    def name(self):
        """
        Gets the name of this ConditionInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this ConditionInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConditionInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this ConditionInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parameters(self):
        """
        Gets the parameters of this ConditionInputV1.
        The parameters for the formula used to create a calculated item. Each parameter should have a format of 'name=id' where 'name' is the variable identifier, without the leading $ sign, and 'id' is the ID of the item referenced by the variable

        :return: The parameters of this ConditionInputV1.
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ConditionInputV1.
        The parameters for the formula used to create a calculated item. Each parameter should have a format of 'name=id' where 'name' is the variable identifier, without the leading $ sign, and 'id' is the ID of the item referenced by the variable

        :param parameters: The parameters of this ConditionInputV1.
        :type: list[str]
        """

        self._parameters = parameters

    @property
    def properties(self):
        """
        Gets the properties of this ConditionInputV1.

        :return: The properties of this ConditionInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ConditionInputV1.

        :param properties: The properties of this ConditionInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._properties = properties

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ConditionInputV1.
        The ID of the workbook to which this item will be scoped.

        :return: The scoped_to of this ConditionInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ConditionInputV1.
        The ID of the workbook to which this item will be scoped.

        :param scoped_to: The scoped_to of this ConditionInputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def security_string(self):
        """
        Gets the security_string of this ConditionInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :return: The security_string of this ConditionInputV1.
        :rtype: str
        """
        return self._security_string

    @security_string.setter
    def security_string(self, security_string):
        """
        Sets the security_string of this ConditionInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :param security_string: The security_string of this ConditionInputV1.
        :type: str
        """

        self._security_string = security_string

    @property
    def source_security_string(self):
        """
        Gets the source_security_string of this ConditionInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :return: The source_security_string of this ConditionInputV1.
        :rtype: str
        """
        return self._source_security_string

    @source_security_string.setter
    def source_security_string(self, source_security_string):
        """
        Sets the source_security_string of this ConditionInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :param source_security_string: The source_security_string of this ConditionInputV1.
        :type: str
        """

        self._source_security_string = source_security_string

    @property
    def sync_token(self):
        """
        Gets the sync_token of this ConditionInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :return: The sync_token of this ConditionInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this ConditionInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this ConditionInputV1.
        :type: str
        """

        self._sync_token = sync_token

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this ConditionInputV1.
        The unit of measure for the keys in a stored condition. Do not set for calculated conditions. The units for calculated conditions are determined by the calculation.

        :return: The unit_of_measure of this ConditionInputV1.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this ConditionInputV1.
        The unit of measure for the keys in a stored condition. Do not set for calculated conditions. The units for calculated conditions are determined by the calculation.

        :param unit_of_measure: The unit_of_measure of this ConditionInputV1.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

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
        if not isinstance(other, ConditionInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
