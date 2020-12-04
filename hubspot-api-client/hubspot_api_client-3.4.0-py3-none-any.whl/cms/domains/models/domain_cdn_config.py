# coding: utf-8

"""
    Domains

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.domains.configuration import Configuration


class DomainCdnConfig(object):
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
        'portal_id': 'int',
        'created': 'int',
        'updated': 'int',
        'domain_id': 'int',
        'cert_id': 'int',
        'cert_expiration_date': 'int',
        'cdn_id': 'str',
        'cdn_group_id': 'str',
        'ssl_status': 'str',
        'validation_method': 'str',
        'http_body': 'str',
        'http_url_path': 'str',
        'cname': 'str',
        'cname_target': 'str',
        'minimum_tls_version': 'str',
        'alternate_origin_hostname': 'str',
        'id': 'int'
    }

    attribute_map = {
        'portal_id': 'portalId',
        'created': 'created',
        'updated': 'updated',
        'domain_id': 'domainId',
        'cert_id': 'certId',
        'cert_expiration_date': 'certExpirationDate',
        'cdn_id': 'cdnId',
        'cdn_group_id': 'cdnGroupId',
        'ssl_status': 'sslStatus',
        'validation_method': 'validationMethod',
        'http_body': 'httpBody',
        'http_url_path': 'httpUrlPath',
        'cname': 'cname',
        'cname_target': 'cnameTarget',
        'minimum_tls_version': 'minimumTlsVersion',
        'alternate_origin_hostname': 'alternateOriginHostname',
        'id': 'id'
    }

    def __init__(self, portal_id=None, created=None, updated=None, domain_id=None, cert_id=None, cert_expiration_date=None, cdn_id=None, cdn_group_id=None, ssl_status=None, validation_method=None, http_body=None, http_url_path=None, cname=None, cname_target=None, minimum_tls_version=None, alternate_origin_hostname=None, id=None, local_vars_configuration=None):  # noqa: E501
        """DomainCdnConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._portal_id = None
        self._created = None
        self._updated = None
        self._domain_id = None
        self._cert_id = None
        self._cert_expiration_date = None
        self._cdn_id = None
        self._cdn_group_id = None
        self._ssl_status = None
        self._validation_method = None
        self._http_body = None
        self._http_url_path = None
        self._cname = None
        self._cname_target = None
        self._minimum_tls_version = None
        self._alternate_origin_hostname = None
        self._id = None
        self.discriminator = None

        self.portal_id = portal_id
        self.created = created
        self.updated = updated
        self.domain_id = domain_id
        self.cert_id = cert_id
        self.cert_expiration_date = cert_expiration_date
        self.cdn_id = cdn_id
        self.cdn_group_id = cdn_group_id
        self.ssl_status = ssl_status
        self.validation_method = validation_method
        self.http_body = http_body
        self.http_url_path = http_url_path
        self.cname = cname
        self.cname_target = cname_target
        self.minimum_tls_version = minimum_tls_version
        self.alternate_origin_hostname = alternate_origin_hostname
        self.id = id

    @property
    def portal_id(self):
        """Gets the portal_id of this DomainCdnConfig.  # noqa: E501


        :return: The portal_id of this DomainCdnConfig.  # noqa: E501
        :rtype: int
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """Sets the portal_id of this DomainCdnConfig.


        :param portal_id: The portal_id of this DomainCdnConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and portal_id is None:  # noqa: E501
            raise ValueError("Invalid value for `portal_id`, must not be `None`")  # noqa: E501

        self._portal_id = portal_id

    @property
    def created(self):
        """Gets the created of this DomainCdnConfig.  # noqa: E501


        :return: The created of this DomainCdnConfig.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DomainCdnConfig.


        :param created: The created of this DomainCdnConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this DomainCdnConfig.  # noqa: E501


        :return: The updated of this DomainCdnConfig.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this DomainCdnConfig.


        :param updated: The updated of this DomainCdnConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and updated is None:  # noqa: E501
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    @property
    def domain_id(self):
        """Gets the domain_id of this DomainCdnConfig.  # noqa: E501


        :return: The domain_id of this DomainCdnConfig.  # noqa: E501
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DomainCdnConfig.


        :param domain_id: The domain_id of this DomainCdnConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and domain_id is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def cert_id(self):
        """Gets the cert_id of this DomainCdnConfig.  # noqa: E501


        :return: The cert_id of this DomainCdnConfig.  # noqa: E501
        :rtype: int
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        """Sets the cert_id of this DomainCdnConfig.


        :param cert_id: The cert_id of this DomainCdnConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cert_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cert_id`, must not be `None`")  # noqa: E501

        self._cert_id = cert_id

    @property
    def cert_expiration_date(self):
        """Gets the cert_expiration_date of this DomainCdnConfig.  # noqa: E501


        :return: The cert_expiration_date of this DomainCdnConfig.  # noqa: E501
        :rtype: int
        """
        return self._cert_expiration_date

    @cert_expiration_date.setter
    def cert_expiration_date(self, cert_expiration_date):
        """Sets the cert_expiration_date of this DomainCdnConfig.


        :param cert_expiration_date: The cert_expiration_date of this DomainCdnConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cert_expiration_date is None:  # noqa: E501
            raise ValueError("Invalid value for `cert_expiration_date`, must not be `None`")  # noqa: E501

        self._cert_expiration_date = cert_expiration_date

    @property
    def cdn_id(self):
        """Gets the cdn_id of this DomainCdnConfig.  # noqa: E501


        :return: The cdn_id of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._cdn_id

    @cdn_id.setter
    def cdn_id(self, cdn_id):
        """Sets the cdn_id of this DomainCdnConfig.


        :param cdn_id: The cdn_id of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cdn_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cdn_id`, must not be `None`")  # noqa: E501

        self._cdn_id = cdn_id

    @property
    def cdn_group_id(self):
        """Gets the cdn_group_id of this DomainCdnConfig.  # noqa: E501


        :return: The cdn_group_id of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._cdn_group_id

    @cdn_group_id.setter
    def cdn_group_id(self, cdn_group_id):
        """Sets the cdn_group_id of this DomainCdnConfig.


        :param cdn_group_id: The cdn_group_id of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cdn_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cdn_group_id`, must not be `None`")  # noqa: E501

        self._cdn_group_id = cdn_group_id

    @property
    def ssl_status(self):
        """Gets the ssl_status of this DomainCdnConfig.  # noqa: E501


        :return: The ssl_status of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._ssl_status

    @ssl_status.setter
    def ssl_status(self, ssl_status):
        """Sets the ssl_status of this DomainCdnConfig.


        :param ssl_status: The ssl_status of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ssl_status is None:  # noqa: E501
            raise ValueError("Invalid value for `ssl_status`, must not be `None`")  # noqa: E501
        allowed_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ssl_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ssl_status` ({0}), must be one of {1}"  # noqa: E501
                .format(ssl_status, allowed_values)
            )

        self._ssl_status = ssl_status

    @property
    def validation_method(self):
        """Gets the validation_method of this DomainCdnConfig.  # noqa: E501


        :return: The validation_method of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._validation_method

    @validation_method.setter
    def validation_method(self, validation_method):
        """Sets the validation_method of this DomainCdnConfig.


        :param validation_method: The validation_method of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and validation_method is None:  # noqa: E501
            raise ValueError("Invalid value for `validation_method`, must not be `None`")  # noqa: E501
        allowed_values = ["0", "1", "2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and validation_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `validation_method` ({0}), must be one of {1}"  # noqa: E501
                .format(validation_method, allowed_values)
            )

        self._validation_method = validation_method

    @property
    def http_body(self):
        """Gets the http_body of this DomainCdnConfig.  # noqa: E501


        :return: The http_body of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._http_body

    @http_body.setter
    def http_body(self, http_body):
        """Sets the http_body of this DomainCdnConfig.


        :param http_body: The http_body of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and http_body is None:  # noqa: E501
            raise ValueError("Invalid value for `http_body`, must not be `None`")  # noqa: E501

        self._http_body = http_body

    @property
    def http_url_path(self):
        """Gets the http_url_path of this DomainCdnConfig.  # noqa: E501


        :return: The http_url_path of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._http_url_path

    @http_url_path.setter
    def http_url_path(self, http_url_path):
        """Sets the http_url_path of this DomainCdnConfig.


        :param http_url_path: The http_url_path of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and http_url_path is None:  # noqa: E501
            raise ValueError("Invalid value for `http_url_path`, must not be `None`")  # noqa: E501

        self._http_url_path = http_url_path

    @property
    def cname(self):
        """Gets the cname of this DomainCdnConfig.  # noqa: E501


        :return: The cname of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this DomainCdnConfig.


        :param cname: The cname of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cname is None:  # noqa: E501
            raise ValueError("Invalid value for `cname`, must not be `None`")  # noqa: E501

        self._cname = cname

    @property
    def cname_target(self):
        """Gets the cname_target of this DomainCdnConfig.  # noqa: E501


        :return: The cname_target of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._cname_target

    @cname_target.setter
    def cname_target(self, cname_target):
        """Sets the cname_target of this DomainCdnConfig.


        :param cname_target: The cname_target of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cname_target is None:  # noqa: E501
            raise ValueError("Invalid value for `cname_target`, must not be `None`")  # noqa: E501

        self._cname_target = cname_target

    @property
    def minimum_tls_version(self):
        """Gets the minimum_tls_version of this DomainCdnConfig.  # noqa: E501


        :return: The minimum_tls_version of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._minimum_tls_version

    @minimum_tls_version.setter
    def minimum_tls_version(self, minimum_tls_version):
        """Sets the minimum_tls_version of this DomainCdnConfig.


        :param minimum_tls_version: The minimum_tls_version of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and minimum_tls_version is None:  # noqa: E501
            raise ValueError("Invalid value for `minimum_tls_version`, must not be `None`")  # noqa: E501
        allowed_values = ["1.0", "1.1", "1.2", "1.3", "none", "null"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and minimum_tls_version not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `minimum_tls_version` ({0}), must be one of {1}"  # noqa: E501
                .format(minimum_tls_version, allowed_values)
            )

        self._minimum_tls_version = minimum_tls_version

    @property
    def alternate_origin_hostname(self):
        """Gets the alternate_origin_hostname of this DomainCdnConfig.  # noqa: E501


        :return: The alternate_origin_hostname of this DomainCdnConfig.  # noqa: E501
        :rtype: str
        """
        return self._alternate_origin_hostname

    @alternate_origin_hostname.setter
    def alternate_origin_hostname(self, alternate_origin_hostname):
        """Sets the alternate_origin_hostname of this DomainCdnConfig.


        :param alternate_origin_hostname: The alternate_origin_hostname of this DomainCdnConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and alternate_origin_hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `alternate_origin_hostname`, must not be `None`")  # noqa: E501

        self._alternate_origin_hostname = alternate_origin_hostname

    @property
    def id(self):
        """Gets the id of this DomainCdnConfig.  # noqa: E501


        :return: The id of this DomainCdnConfig.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainCdnConfig.


        :param id: The id of this DomainCdnConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DomainCdnConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainCdnConfig):
            return True

        return self.to_dict() != other.to_dict()
