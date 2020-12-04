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


class AgentStatusV1(object):
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
        'connections': 'list[ConnectionStatusV1]',
        'id': 'str',
        'status': 'str',
        'version': 'str'
    }

    attribute_map = {
        'connections': 'connections',
        'id': 'id',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, connections=None, id=None, status=None, version=None):
        """
        AgentStatusV1 - a model defined in Swagger
        """

        self._connections = None
        self._id = None
        self._status = None
        self._version = None

        if connections is not None:
          self.connections = connections
        if id is not None:
          self.id = id
        if status is not None:
          self.status = status
        if version is not None:
          self.version = version

    @property
    def connections(self):
        """
        Gets the connections of this AgentStatusV1.
        The status for each connection known by the agent

        :return: The connections of this AgentStatusV1.
        :rtype: list[ConnectionStatusV1]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """
        Sets the connections of this AgentStatusV1.
        The status for each connection known by the agent

        :param connections: The connections of this AgentStatusV1.
        :type: list[ConnectionStatusV1]
        """
        if connections is None:
            raise ValueError("Invalid value for `connections`, must not be `None`")

        self._connections = connections

    @property
    def id(self):
        """
        Gets the id of this AgentStatusV1.
        The ID of the agent. This ID uniquely identifies this agent but does not convey any information about the agent. There is no specified structure for this ID; it may be in UUID form but need not be.

        :return: The id of this AgentStatusV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AgentStatusV1.
        The ID of the agent. This ID uniquely identifies this agent but does not convey any information about the agent. There is no specified structure for this ID; it may be in UUID form but need not be.

        :param id: The id of this AgentStatusV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def status(self):
        """
        Gets the status of this AgentStatusV1.
        The status of the current connection between the agent and the Seeq application server. Valid values are Connected, Disconnected and Connecting.If the state is Disconnected, see disconnectReason.

        :return: The status of this AgentStatusV1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AgentStatusV1.
        The status of the current connection between the agent and the Seeq application server. Valid values are Connected, Disconnected and Connecting.If the state is Disconnected, see disconnectReason.

        :param status: The status of this AgentStatusV1.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def version(self):
        """
        Gets the version of this AgentStatusV1.
        The Seeq version of the agent

        :return: The version of this AgentStatusV1.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AgentStatusV1.
        The Seeq version of the agent

        :param version: The version of this AgentStatusV1.
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
        if not isinstance(other, AgentStatusV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
