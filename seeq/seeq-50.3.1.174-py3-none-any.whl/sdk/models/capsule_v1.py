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


class CapsuleV1(object):
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
        'cursor_key': 'object',
        'end': 'object',
        'id': 'str',
        'is_uncertain': 'bool',
        'properties': 'list[ScalarPropertyV1]',
        'start': 'object'
    }

    attribute_map = {
        'cursor_key': 'cursorKey',
        'end': 'end',
        'id': 'id',
        'is_uncertain': 'isUncertain',
        'properties': 'properties',
        'start': 'start'
    }

    def __init__(self, cursor_key=None, end=None, id=None, is_uncertain=None, properties=None, start=None):
        """
        CapsuleV1 - a model defined in Swagger
        """

        self._cursor_key = None
        self._end = None
        self._id = None
        self._is_uncertain = None
        self._properties = None
        self._start = None

        if cursor_key is not None:
          self.cursor_key = cursor_key
        if end is not None:
          self.end = end
        if id is not None:
          self.id = id
        if is_uncertain is not None:
          self.is_uncertain = is_uncertain
        if properties is not None:
          self.properties = properties
        if start is not None:
          self.start = start

    @property
    def cursor_key(self):
        """
        Gets the cursor_key of this CapsuleV1.
        The point at which the capsule becomes uncertain. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :return: The cursor_key of this CapsuleV1.
        :rtype: object
        """
        return self._cursor_key

    @cursor_key.setter
    def cursor_key(self, cursor_key):
        """
        Sets the cursor_key of this CapsuleV1.
        The point at which the capsule becomes uncertain. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :param cursor_key: The cursor_key of this CapsuleV1.
        :type: object
        """

        self._cursor_key = cursor_key

    @property
    def end(self):
        """
        Gets the end of this CapsuleV1.
        The end of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :return: The end of this CapsuleV1.
        :rtype: object
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this CapsuleV1.
        The end of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :param end: The end of this CapsuleV1.
        :type: object
        """

        self._end = end

    @property
    def id(self):
        """
        Gets the id of this CapsuleV1.
        The id of the capsule

        :return: The id of this CapsuleV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CapsuleV1.
        The id of the capsule

        :param id: The id of this CapsuleV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_uncertain(self):
        """
        Gets the is_uncertain of this CapsuleV1.
        True if this capsule is fully or partially uncertain

        :return: The is_uncertain of this CapsuleV1.
        :rtype: bool
        """
        return self._is_uncertain

    @is_uncertain.setter
    def is_uncertain(self, is_uncertain):
        """
        Sets the is_uncertain of this CapsuleV1.
        True if this capsule is fully or partially uncertain

        :param is_uncertain: The is_uncertain of this CapsuleV1.
        :type: bool
        """

        self._is_uncertain = is_uncertain

    @property
    def properties(self):
        """
        Gets the properties of this CapsuleV1.
        A list of the capsule's properties

        :return: The properties of this CapsuleV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CapsuleV1.
        A list of the capsule's properties

        :param properties: The properties of this CapsuleV1.
        :type: list[ScalarPropertyV1]
        """

        self._properties = properties

    @property
    def start(self):
        """
        Gets the start of this CapsuleV1.
        The start of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :return: The start of this CapsuleV1.
        :rtype: object
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this CapsuleV1.
        The start of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :param start: The start of this CapsuleV1.
        :type: object
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")

        self._start = start

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
        if not isinstance(other, CapsuleV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
