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


class CapsulesOutputV1(object):
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
        'capsules': 'list[CapsuleV1]',
        'graph_limit': 'int',
        'has_items_before_offset_present': 'bool',
        'key_unit_of_measure': 'str',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'status_message': 'str',
        'warning_count': 'int',
        'warning_logs': 'list[FormulaLogV1]'
    }

    attribute_map = {
        'capsules': 'capsules',
        'graph_limit': 'graphLimit',
        'has_items_before_offset_present': 'hasItemsBeforeOffsetPresent',
        'key_unit_of_measure': 'keyUnitOfMeasure',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'status_message': 'statusMessage',
        'warning_count': 'warningCount',
        'warning_logs': 'warningLogs'
    }

    def __init__(self, capsules=None, graph_limit=None, has_items_before_offset_present=False, key_unit_of_measure=None, limit=None, next=None, offset=None, prev=None, status_message=None, warning_count=None, warning_logs=None):
        """
        CapsulesOutputV1 - a model defined in Swagger
        """

        self._capsules = None
        self._graph_limit = None
        self._has_items_before_offset_present = None
        self._key_unit_of_measure = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._status_message = None
        self._warning_count = None
        self._warning_logs = None

        if capsules is not None:
          self.capsules = capsules
        if graph_limit is not None:
          self.graph_limit = graph_limit
        if has_items_before_offset_present is not None:
          self.has_items_before_offset_present = has_items_before_offset_present
        if key_unit_of_measure is not None:
          self.key_unit_of_measure = key_unit_of_measure
        if limit is not None:
          self.limit = limit
        if next is not None:
          self.next = next
        if offset is not None:
          self.offset = offset
        if prev is not None:
          self.prev = prev
        if status_message is not None:
          self.status_message = status_message
        if warning_count is not None:
          self.warning_count = warning_count
        if warning_logs is not None:
          self.warning_logs = warning_logs

    @property
    def capsules(self):
        """
        Gets the capsules of this CapsulesOutputV1.
        The list of capsules

        :return: The capsules of this CapsulesOutputV1.
        :rtype: list[CapsuleV1]
        """
        return self._capsules

    @capsules.setter
    def capsules(self, capsules):
        """
        Sets the capsules of this CapsulesOutputV1.
        The list of capsules

        :param capsules: The capsules of this CapsulesOutputV1.
        :type: list[CapsuleV1]
        """
        if capsules is None:
            raise ValueError("Invalid value for `capsules`, must not be `None`")

        self._capsules = capsules

    @property
    def graph_limit(self):
        """
        Gets the graph_limit of this CapsulesOutputV1.

        :return: The graph_limit of this CapsulesOutputV1.
        :rtype: int
        """
        return self._graph_limit

    @graph_limit.setter
    def graph_limit(self, graph_limit):
        """
        Sets the graph_limit of this CapsulesOutputV1.

        :param graph_limit: The graph_limit of this CapsulesOutputV1.
        :type: int
        """

        self._graph_limit = graph_limit

    @property
    def has_items_before_offset_present(self):
        """
        Gets the has_items_before_offset_present of this CapsulesOutputV1.

        :return: The has_items_before_offset_present of this CapsulesOutputV1.
        :rtype: bool
        """
        return self._has_items_before_offset_present

    @has_items_before_offset_present.setter
    def has_items_before_offset_present(self, has_items_before_offset_present):
        """
        Sets the has_items_before_offset_present of this CapsulesOutputV1.

        :param has_items_before_offset_present: The has_items_before_offset_present of this CapsulesOutputV1.
        :type: bool
        """

        self._has_items_before_offset_present = has_items_before_offset_present

    @property
    def key_unit_of_measure(self):
        """
        Gets the key_unit_of_measure of this CapsulesOutputV1.
        The unit of measure for the capsule starts and ends. If left empty, input is assumed to be in ISO8601 format.

        :return: The key_unit_of_measure of this CapsulesOutputV1.
        :rtype: str
        """
        return self._key_unit_of_measure

    @key_unit_of_measure.setter
    def key_unit_of_measure(self, key_unit_of_measure):
        """
        Sets the key_unit_of_measure of this CapsulesOutputV1.
        The unit of measure for the capsule starts and ends. If left empty, input is assumed to be in ISO8601 format.

        :param key_unit_of_measure: The key_unit_of_measure of this CapsulesOutputV1.
        :type: str
        """

        self._key_unit_of_measure = key_unit_of_measure

    @property
    def limit(self):
        """
        Gets the limit of this CapsulesOutputV1.
        The pagination limit, the total number of collection items that will be returned in this page of results

        :return: The limit of this CapsulesOutputV1.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CapsulesOutputV1.
        The pagination limit, the total number of collection items that will be returned in this page of results

        :param limit: The limit of this CapsulesOutputV1.
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """
        Gets the next of this CapsulesOutputV1.
        The href of the next set of paginated results

        :return: The next of this CapsulesOutputV1.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this CapsulesOutputV1.
        The href of the next set of paginated results

        :param next: The next of this CapsulesOutputV1.
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """
        Gets the offset of this CapsulesOutputV1.
        The pagination offset, the index of the first collection item that will be returned in this page of results

        :return: The offset of this CapsulesOutputV1.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this CapsulesOutputV1.
        The pagination offset, the index of the first collection item that will be returned in this page of results

        :param offset: The offset of this CapsulesOutputV1.
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """
        Gets the prev of this CapsulesOutputV1.
        The href of the previous set of paginated results

        :return: The prev of this CapsulesOutputV1.
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """
        Sets the prev of this CapsulesOutputV1.
        The href of the previous set of paginated results

        :param prev: The prev of this CapsulesOutputV1.
        :type: str
        """

        self._prev = prev

    @property
    def status_message(self):
        """
        Gets the status_message of this CapsulesOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this CapsulesOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this CapsulesOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this CapsulesOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def warning_count(self):
        """
        Gets the warning_count of this CapsulesOutputV1.
        The total number of warnings that have occurred

        :return: The warning_count of this CapsulesOutputV1.
        :rtype: int
        """
        return self._warning_count

    @warning_count.setter
    def warning_count(self, warning_count):
        """
        Sets the warning_count of this CapsulesOutputV1.
        The total number of warnings that have occurred

        :param warning_count: The warning_count of this CapsulesOutputV1.
        :type: int
        """

        self._warning_count = warning_count

    @property
    def warning_logs(self):
        """
        Gets the warning_logs of this CapsulesOutputV1.
        The Formula warning logs, which includes the text, line number, and column number where the warning occurred in addition to the warning details

        :return: The warning_logs of this CapsulesOutputV1.
        :rtype: list[FormulaLogV1]
        """
        return self._warning_logs

    @warning_logs.setter
    def warning_logs(self, warning_logs):
        """
        Sets the warning_logs of this CapsulesOutputV1.
        The Formula warning logs, which includes the text, line number, and column number where the warning occurred in addition to the warning details

        :param warning_logs: The warning_logs of this CapsulesOutputV1.
        :type: list[FormulaLogV1]
        """

        self._warning_logs = warning_logs

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
        if not isinstance(other, CapsulesOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
