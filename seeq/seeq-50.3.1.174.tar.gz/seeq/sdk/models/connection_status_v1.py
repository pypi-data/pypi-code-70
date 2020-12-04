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


class ConnectionStatusV1(object):
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
        'datasource_class': 'str',
        'datasource_id': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'sync_progress': 'SyncProgress',
        'sync_status': 'str'
    }

    attribute_map = {
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'sync_progress': 'syncProgress',
        'sync_status': 'syncStatus'
    }

    def __init__(self, datasource_class=None, datasource_id=None, id=None, name=None, status=None, sync_progress=None, sync_status=None):
        """
        ConnectionStatusV1 - a model defined in Swagger
        """

        self._datasource_class = None
        self._datasource_id = None
        self._id = None
        self._name = None
        self._status = None
        self._sync_progress = None
        self._sync_status = None

        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if status is not None:
          self.status = status
        if sync_progress is not None:
          self.sync_progress = sync_progress
        if sync_status is not None:
          self.sync_status = sync_status

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this ConnectionStatusV1.
        The datasource class served by this connector.  Example: OSIsoft PI

        :return: The datasource_class of this ConnectionStatusV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this ConnectionStatusV1.
        The datasource class served by this connector.  Example: OSIsoft PI

        :param datasource_class: The datasource_class of this ConnectionStatusV1.
        :type: str
        """
        if datasource_class is None:
            raise ValueError("Invalid value for `datasource_class`, must not be `None`")

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this ConnectionStatusV1.
        The datasource ID served by this connector.

        :return: The datasource_id of this ConnectionStatusV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this ConnectionStatusV1.
        The datasource ID served by this connector.

        :param datasource_id: The datasource_id of this ConnectionStatusV1.
        :type: str
        """
        if datasource_id is None:
            raise ValueError("Invalid value for `datasource_id`, must not be `None`")

        self._datasource_id = datasource_id

    @property
    def id(self):
        """
        Gets the id of this ConnectionStatusV1.
        The ID of the connector. This ID uniquely identifies this connector but does not convey any information about the connector. There is no specified structure for this ID; it may be in UUID form but need not be.

        :return: The id of this ConnectionStatusV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionStatusV1.
        The ID of the connector. This ID uniquely identifies this connector but does not convey any information about the connector. There is no specified structure for this ID; it may be in UUID form but need not be.

        :param id: The id of this ConnectionStatusV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ConnectionStatusV1.
        The name of this connector. The name should represent the specific data source to which this connector connects.  Example: AMAZONA-4RV912N

        :return: The name of this ConnectionStatusV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectionStatusV1.
        The name of this connector. The name should represent the specific data source to which this connector connects.  Example: AMAZONA-4RV912N

        :param name: The name of this ConnectionStatusV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this ConnectionStatusV1.
        The status of the current connection between the datasource and this connector. Valid values are Connected, Disconnected and Connecting. If the state is Disconnected (or Connecting), it could be caused by a failure in the connection between the connector and its datasource or a failed connection between the Seeq application server and the agent hosting this connector. See disconnectReason.

        :return: The status of this ConnectionStatusV1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConnectionStatusV1.
        The status of the current connection between the datasource and this connector. Valid values are Connected, Disconnected and Connecting. If the state is Disconnected (or Connecting), it could be caused by a failure in the connection between the connector and its datasource or a failed connection between the Seeq application server and the agent hosting this connector. See disconnectReason.

        :param status: The status of this ConnectionStatusV1.
        :type: str
        """

        self._status = status

    @property
    def sync_progress(self):
        """
        Gets the sync_progress of this ConnectionStatusV1.
        Metadata sync progress and total items synced from an external datasource to Seeq

        :return: The sync_progress of this ConnectionStatusV1.
        :rtype: SyncProgress
        """
        return self._sync_progress

    @sync_progress.setter
    def sync_progress(self, sync_progress):
        """
        Sets the sync_progress of this ConnectionStatusV1.
        Metadata sync progress and total items synced from an external datasource to Seeq

        :param sync_progress: The sync_progress of this ConnectionStatusV1.
        :type: SyncProgress
        """

        self._sync_progress = sync_progress

    @property
    def sync_status(self):
        """
        Gets the sync_status of this ConnectionStatusV1.
        The synchronization status of the current connection between the datasource and this connector. Valid values are UNKNOWN, SYNC_INITIALIZING, SYNC_IN_PROGRESS, SYNC_COMPLETE, SYNC_ARCHIVING_DELETED_ITEMS. 

        :return: The sync_status of this ConnectionStatusV1.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """
        Sets the sync_status of this ConnectionStatusV1.
        The synchronization status of the current connection between the datasource and this connector. Valid values are UNKNOWN, SYNC_INITIALIZING, SYNC_IN_PROGRESS, SYNC_COMPLETE, SYNC_ARCHIVING_DELETED_ITEMS. 

        :param sync_status: The sync_status of this ConnectionStatusV1.
        :type: str
        """

        self._sync_status = sync_status

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
        if not isinstance(other, ConnectionStatusV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
