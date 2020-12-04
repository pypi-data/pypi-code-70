# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.48.10-BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ArchiveSignalOutputV1(object):
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
        'newly_archived': 'bool',
        'status_message': 'str'
    }

    attribute_map = {
        'newly_archived': 'newlyArchived',
        'status_message': 'statusMessage'
    }

    def __init__(self, newly_archived=False, status_message=None):
        """
        ArchiveSignalOutputV1 - a model defined in Swagger
        """

        self._newly_archived = None
        self._status_message = None

        if newly_archived is not None:
          self.newly_archived = newly_archived
        if status_message is not None:
          self.status_message = status_message

    @property
    def newly_archived(self):
        """
        Gets the newly_archived of this ArchiveSignalOutputV1.
        true if the signal was newly archived; false if the signal was already archived

        :return: The newly_archived of this ArchiveSignalOutputV1.
        :rtype: bool
        """
        return self._newly_archived

    @newly_archived.setter
    def newly_archived(self, newly_archived):
        """
        Sets the newly_archived of this ArchiveSignalOutputV1.
        true if the signal was newly archived; false if the signal was already archived

        :param newly_archived: The newly_archived of this ArchiveSignalOutputV1.
        :type: bool
        """

        self._newly_archived = newly_archived

    @property
    def status_message(self):
        """
        Gets the status_message of this ArchiveSignalOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this ArchiveSignalOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ArchiveSignalOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this ArchiveSignalOutputV1.
        :type: str
        """

        self._status_message = status_message

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
        if not isinstance(other, ArchiveSignalOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
