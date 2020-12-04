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


class ActivityGraphOutputV1(object):
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
        'edges': 'list[ActivityGraphEdgeOutputV1]',
        'nodes': 'list[ActivityOutputV1]'
    }

    attribute_map = {
        'edges': 'edges',
        'nodes': 'nodes'
    }

    def __init__(self, edges=None, nodes=None):
        """
        ActivityGraphOutputV1 - a model defined in Swagger
        """

        self._edges = None
        self._nodes = None

        if edges is not None:
          self.edges = edges
        if nodes is not None:
          self.nodes = nodes

    @property
    def edges(self):
        """
        Gets the edges of this ActivityGraphOutputV1.
        The current graph of Activities for the request. The IDs referenced in the edges correspond to the IDs of the objects found in the nodes. The graph is a directed acyclic graph.

        :return: The edges of this ActivityGraphOutputV1.
        :rtype: list[ActivityGraphEdgeOutputV1]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """
        Sets the edges of this ActivityGraphOutputV1.
        The current graph of Activities for the request. The IDs referenced in the edges correspond to the IDs of the objects found in the nodes. The graph is a directed acyclic graph.

        :param edges: The edges of this ActivityGraphOutputV1.
        :type: list[ActivityGraphEdgeOutputV1]
        """

        self._edges = edges

    @property
    def nodes(self):
        """
        Gets the nodes of this ActivityGraphOutputV1.
        The set of Activities in the graph. Each ID in the nodes will be unique in this list. The order is not guaranteed to be meaningful. Correspond the IDs with  edges to determine current leaf Activities.

        :return: The nodes of this ActivityGraphOutputV1.
        :rtype: list[ActivityOutputV1]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this ActivityGraphOutputV1.
        The set of Activities in the graph. Each ID in the nodes will be unique in this list. The order is not guaranteed to be meaningful. Correspond the IDs with  edges to determine current leaf Activities.

        :param nodes: The nodes of this ActivityGraphOutputV1.
        :type: list[ActivityOutputV1]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")

        self._nodes = nodes

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
        if not isinstance(other, ActivityGraphOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
