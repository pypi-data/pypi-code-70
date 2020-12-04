# coding: utf-8

"""
Influx API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 0.1.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class OrganizationLinks(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        '_self': 'str',
        'members': 'str',
        'owners': 'str',
        'labels': 'str',
        'secrets': 'str',
        'buckets': 'str',
        'tasks': 'str',
        'dashboards': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'members': 'members',
        'owners': 'owners',
        'labels': 'labels',
        'secrets': 'secrets',
        'buckets': 'buckets',
        'tasks': 'tasks',
        'dashboards': 'dashboards'
    }

    def __init__(self, _self=None, members=None, owners=None, labels=None, secrets=None, buckets=None, tasks=None, dashboards=None):  # noqa: E501,D401,D403
        """OrganizationLinks - a model defined in OpenAPI."""  # noqa: E501
        self.__self = None
        self._members = None
        self._owners = None
        self._labels = None
        self._secrets = None
        self._buckets = None
        self._tasks = None
        self._dashboards = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if members is not None:
            self.members = members
        if owners is not None:
            self.owners = owners
        if labels is not None:
            self.labels = labels
        if secrets is not None:
            self.secrets = secrets
        if buckets is not None:
            self.buckets = buckets
        if tasks is not None:
            self.tasks = tasks
        if dashboards is not None:
            self.dashboards = dashboards

    @property
    def _self(self):
        """Get the _self of this OrganizationLinks.

        URI of resource.

        :return: The _self of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Set the _self of this OrganizationLinks.

        URI of resource.

        :param _self: The _self of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self.__self = _self

    @property
    def members(self):
        """Get the members of this OrganizationLinks.

        URI of resource.

        :return: The members of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self._members

    @members.setter
    def members(self, members):
        """Set the members of this OrganizationLinks.

        URI of resource.

        :param members: The members of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self._members = members

    @property
    def owners(self):
        """Get the owners of this OrganizationLinks.

        URI of resource.

        :return: The owners of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Set the owners of this OrganizationLinks.

        URI of resource.

        :param owners: The owners of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self._owners = owners

    @property
    def labels(self):
        """Get the labels of this OrganizationLinks.

        URI of resource.

        :return: The labels of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this OrganizationLinks.

        URI of resource.

        :param labels: The labels of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self._labels = labels

    @property
    def secrets(self):
        """Get the secrets of this OrganizationLinks.

        URI of resource.

        :return: The secrets of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Set the secrets of this OrganizationLinks.

        URI of resource.

        :param secrets: The secrets of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self._secrets = secrets

    @property
    def buckets(self):
        """Get the buckets of this OrganizationLinks.

        URI of resource.

        :return: The buckets of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Set the buckets of this OrganizationLinks.

        URI of resource.

        :param buckets: The buckets of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self._buckets = buckets

    @property
    def tasks(self):
        """Get the tasks of this OrganizationLinks.

        URI of resource.

        :return: The tasks of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Set the tasks of this OrganizationLinks.

        URI of resource.

        :param tasks: The tasks of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self._tasks = tasks

    @property
    def dashboards(self):
        """Get the dashboards of this OrganizationLinks.

        URI of resource.

        :return: The dashboards of this OrganizationLinks.
        :rtype: str
        """  # noqa: E501
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Set the dashboards of this OrganizationLinks.

        URI of resource.

        :param dashboards: The dashboards of this OrganizationLinks.
        :type: str
        """  # noqa: E501
        self._dashboards = dashboards

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, OrganizationLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
