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


class AncillaryItemOutputV1(object):
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
        'href': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'order': 'int',
        'type': 'str'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'order': 'order',
        'type': 'type'
    }

    def __init__(self, href=None, id=None, is_archived=False, is_redacted=False, name=None, order=None, type=None):
        """
        AncillaryItemOutputV1 - a model defined in Swagger
        """

        self._href = None
        self._id = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._order = None
        self._type = None

        if href is not None:
          self.href = href
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if order is not None:
          self.order = order
        if type is not None:
          self.type = type

    @property
    def href(self):
        """
        Gets the href of this AncillaryItemOutputV1.
        The href that can be used to interact with the item

        :return: The href of this AncillaryItemOutputV1.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this AncillaryItemOutputV1.
        The href that can be used to interact with the item

        :param href: The href of this AncillaryItemOutputV1.
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def id(self):
        """
        Gets the id of this AncillaryItemOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this AncillaryItemOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AncillaryItemOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this AncillaryItemOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this AncillaryItemOutputV1.
        Whether item is archived

        :return: The is_archived of this AncillaryItemOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this AncillaryItemOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this AncillaryItemOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this AncillaryItemOutputV1.
        Whether item is redacted

        :return: The is_redacted of this AncillaryItemOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this AncillaryItemOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this AncillaryItemOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this AncillaryItemOutputV1.
        The human readable name

        :return: The name of this AncillaryItemOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AncillaryItemOutputV1.
        The human readable name

        :param name: The name of this AncillaryItemOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def order(self):
        """
        Gets the order of this AncillaryItemOutputV1.
        The order for the ancillary, if specified

        :return: The order of this AncillaryItemOutputV1.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this AncillaryItemOutputV1.
        The order for the ancillary, if specified

        :param order: The order of this AncillaryItemOutputV1.
        :type: int
        """

        self._order = order

    @property
    def type(self):
        """
        Gets the type of this AncillaryItemOutputV1.
        The type of the item

        :return: The type of this AncillaryItemOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AncillaryItemOutputV1.
        The type of the item

        :param type: The type of this AncillaryItemOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, AncillaryItemOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
