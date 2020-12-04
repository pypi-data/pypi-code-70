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
from influxdb_client.domain.scraper_target_request import ScraperTargetRequest


class ScraperTargetResponse(ScraperTargetRequest):
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
        'id': 'str',
        'org': 'str',
        'bucket': 'str',
        'links': 'object',
        'name': 'str',
        'type': 'str',
        'url': 'str',
        'org_id': 'str',
        'bucket_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'org': 'org',
        'bucket': 'bucket',
        'links': 'links',
        'name': 'name',
        'type': 'type',
        'url': 'url',
        'org_id': 'orgID',
        'bucket_id': 'bucketID'
    }

    def __init__(self, id=None, org=None, bucket=None, links=None, name=None, type=None, url=None, org_id=None, bucket_id=None):  # noqa: E501,D401,D403
        """ScraperTargetResponse - a model defined in OpenAPI."""  # noqa: E501
        ScraperTargetRequest.__init__(self, name=name, type=type, url=url, org_id=org_id, bucket_id=bucket_id)  # noqa: E501

        self._id = None
        self._org = None
        self._bucket = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if org is not None:
            self.org = org
        if bucket is not None:
            self.bucket = bucket
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Get the id of this ScraperTargetResponse.

        :return: The id of this ScraperTargetResponse.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this ScraperTargetResponse.

        :param id: The id of this ScraperTargetResponse.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def org(self):
        """Get the org of this ScraperTargetResponse.

        The organization name.

        :return: The org of this ScraperTargetResponse.
        :rtype: str
        """  # noqa: E501
        return self._org

    @org.setter
    def org(self, org):
        """Set the org of this ScraperTargetResponse.

        The organization name.

        :param org: The org of this ScraperTargetResponse.
        :type: str
        """  # noqa: E501
        self._org = org

    @property
    def bucket(self):
        """Get the bucket of this ScraperTargetResponse.

        The bucket name.

        :return: The bucket of this ScraperTargetResponse.
        :rtype: str
        """  # noqa: E501
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Set the bucket of this ScraperTargetResponse.

        The bucket name.

        :param bucket: The bucket of this ScraperTargetResponse.
        :type: str
        """  # noqa: E501
        self._bucket = bucket

    @property
    def links(self):
        """Get the links of this ScraperTargetResponse.

        :return: The links of this ScraperTargetResponse.
        :rtype: object
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this ScraperTargetResponse.

        :param links: The links of this ScraperTargetResponse.
        :type: object
        """  # noqa: E501
        self._links = links

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
        if not isinstance(other, ScraperTargetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
