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


class SeeAlsoModel(object):
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
        'children': 'list[SeeAlsoModel]',
        'documentation_href': 'str',
        'short_description': 'str',
        'title': 'str'
    }

    attribute_map = {
        'children': 'children',
        'documentation_href': 'documentationHref',
        'short_description': 'shortDescription',
        'title': 'title'
    }

    def __init__(self, children=None, documentation_href=None, short_description=None, title=None):
        """
        SeeAlsoModel - a model defined in Swagger
        """

        self._children = None
        self._documentation_href = None
        self._short_description = None
        self._title = None

        if children is not None:
          self.children = children
        if documentation_href is not None:
          self.documentation_href = documentation_href
        if short_description is not None:
          self.short_description = short_description
        if title is not None:
          self.title = title

    @property
    def children(self):
        """
        Gets the children of this SeeAlsoModel.

        :return: The children of this SeeAlsoModel.
        :rtype: list[SeeAlsoModel]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this SeeAlsoModel.

        :param children: The children of this SeeAlsoModel.
        :type: list[SeeAlsoModel]
        """

        self._children = children

    @property
    def documentation_href(self):
        """
        Gets the documentation_href of this SeeAlsoModel.

        :return: The documentation_href of this SeeAlsoModel.
        :rtype: str
        """
        return self._documentation_href

    @documentation_href.setter
    def documentation_href(self, documentation_href):
        """
        Sets the documentation_href of this SeeAlsoModel.

        :param documentation_href: The documentation_href of this SeeAlsoModel.
        :type: str
        """

        self._documentation_href = documentation_href

    @property
    def short_description(self):
        """
        Gets the short_description of this SeeAlsoModel.

        :return: The short_description of this SeeAlsoModel.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this SeeAlsoModel.

        :param short_description: The short_description of this SeeAlsoModel.
        :type: str
        """

        self._short_description = short_description

    @property
    def title(self):
        """
        Gets the title of this SeeAlsoModel.

        :return: The title of this SeeAlsoModel.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this SeeAlsoModel.

        :param title: The title of this SeeAlsoModel.
        :type: str
        """

        self._title = title

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
        if not isinstance(other, SeeAlsoModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
