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


class ExternalToolInputV1(object):
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
        'description': 'str',
        'icon_class': 'str',
        'link_type': 'str',
        'name': 'str',
        'reuse_window': 'bool',
        'sort_key': 'str',
        'target_url': 'str',
        'window_details': 'str'
    }

    attribute_map = {
        'description': 'description',
        'icon_class': 'iconClass',
        'link_type': 'linkType',
        'name': 'name',
        'reuse_window': 'reuseWindow',
        'sort_key': 'sortKey',
        'target_url': 'targetUrl',
        'window_details': 'windowDetails'
    }

    def __init__(self, description=None, icon_class=None, link_type=None, name=None, reuse_window=False, sort_key=None, target_url=None, window_details=None):
        """
        ExternalToolInputV1 - a model defined in Swagger
        """

        self._description = None
        self._icon_class = None
        self._link_type = None
        self._name = None
        self._reuse_window = None
        self._sort_key = None
        self._target_url = None
        self._window_details = None

        if description is not None:
          self.description = description
        if icon_class is not None:
          self.icon_class = icon_class
        if link_type is not None:
          self.link_type = link_type
        if name is not None:
          self.name = name
        if reuse_window is not None:
          self.reuse_window = reuse_window
        if sort_key is not None:
          self.sort_key = sort_key
        if target_url is not None:
          self.target_url = target_url
        if window_details is not None:
          self.window_details = window_details

    @property
    def description(self):
        """
        Gets the description of this ExternalToolInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :return: The description of this ExternalToolInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExternalToolInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :param description: The description of this ExternalToolInputV1.
        :type: str
        """

        self._description = description

    @property
    def icon_class(self):
        """
        Gets the icon_class of this ExternalToolInputV1.
        The icon class to be displayed for the external tool (e.g. 'fa fa-magic')

        :return: The icon_class of this ExternalToolInputV1.
        :rtype: str
        """
        return self._icon_class

    @icon_class.setter
    def icon_class(self, icon_class):
        """
        Sets the icon_class of this ExternalToolInputV1.
        The icon class to be displayed for the external tool (e.g. 'fa fa-magic')

        :param icon_class: The icon_class of this ExternalToolInputV1.
        :type: str
        """
        if icon_class is None:
            raise ValueError("Invalid value for `icon_class`, must not be `None`")

        self._icon_class = icon_class

    @property
    def link_type(self):
        """
        Gets the link_type of this ExternalToolInputV1.
        External tool link type. Can be one of 'window', 'tab' or 'none'. When not specified it defaults to 'window'

        :return: The link_type of this ExternalToolInputV1.
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """
        Sets the link_type of this ExternalToolInputV1.
        External tool link type. Can be one of 'window', 'tab' or 'none'. When not specified it defaults to 'window'

        :param link_type: The link_type of this ExternalToolInputV1.
        :type: str
        """

        self._link_type = link_type

    @property
    def name(self):
        """
        Gets the name of this ExternalToolInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this ExternalToolInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalToolInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this ExternalToolInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def reuse_window(self):
        """
        Gets the reuse_window of this ExternalToolInputV1.
        Whether the window is reused if already opened. Only used when 'linkType' is set to 'window'. Defaults to false.

        :return: The reuse_window of this ExternalToolInputV1.
        :rtype: bool
        """
        return self._reuse_window

    @reuse_window.setter
    def reuse_window(self, reuse_window):
        """
        Sets the reuse_window of this ExternalToolInputV1.
        Whether the window is reused if already opened. Only used when 'linkType' is set to 'window'. Defaults to false.

        :param reuse_window: The reuse_window of this ExternalToolInputV1.
        :type: bool
        """

        self._reuse_window = reuse_window

    @property
    def sort_key(self):
        """
        Gets the sort_key of this ExternalToolInputV1.
        Determines the order in which External Tools are displayed in the tool panel

        :return: The sort_key of this ExternalToolInputV1.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """
        Sets the sort_key of this ExternalToolInputV1.
        Determines the order in which External Tools are displayed in the tool panel

        :param sort_key: The sort_key of this ExternalToolInputV1.
        :type: str
        """
        if sort_key is None:
            raise ValueError("Invalid value for `sort_key`, must not be `None`")

        self._sort_key = sort_key

    @property
    def target_url(self):
        """
        Gets the target_url of this ExternalToolInputV1.
        URL of the target application

        :return: The target_url of this ExternalToolInputV1.
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """
        Sets the target_url of this ExternalToolInputV1.
        URL of the target application

        :param target_url: The target_url of this ExternalToolInputV1.
        :type: str
        """
        if target_url is None:
            raise ValueError("Invalid value for `target_url`, must not be `None`")

        self._target_url = target_url

    @property
    def window_details(self):
        """
        Gets the window_details of this ExternalToolInputV1.
        Display characteristics used when 'linkType' is set to 'window'.

        :return: The window_details of this ExternalToolInputV1.
        :rtype: str
        """
        return self._window_details

    @window_details.setter
    def window_details(self, window_details):
        """
        Sets the window_details of this ExternalToolInputV1.
        Display characteristics used when 'linkType' is set to 'window'.

        :param window_details: The window_details of this ExternalToolInputV1.
        :type: str
        """

        self._window_details = window_details

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
        if not isinstance(other, ExternalToolInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
