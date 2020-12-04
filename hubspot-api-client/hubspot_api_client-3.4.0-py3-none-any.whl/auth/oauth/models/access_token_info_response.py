# coding: utf-8

"""
    OAuthService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.auth.oauth.configuration import Configuration


class AccessTokenInfoResponse(object):
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
        'token': 'str',
        'user': 'str',
        'hub_domain': 'str',
        'scopes': 'list[str]',
        'scope_to_scope_group_pks': 'list[int]',
        'hub_id': 'int',
        'app_id': 'int',
        'expires_in': 'int',
        'user_id': 'int',
        'token_type': 'str'
    }

    attribute_map = {
        'token': 'token',
        'user': 'user',
        'hub_domain': 'hub_domain',
        'scopes': 'scopes',
        'scope_to_scope_group_pks': 'scope_to_scope_group_pks',
        'hub_id': 'hub_id',
        'app_id': 'app_id',
        'expires_in': 'expires_in',
        'user_id': 'user_id',
        'token_type': 'token_type'
    }

    def __init__(self, token=None, user=None, hub_domain=None, scopes=None, scope_to_scope_group_pks=None, hub_id=None, app_id=None, expires_in=None, user_id=None, token_type=None, local_vars_configuration=None):  # noqa: E501
        """AccessTokenInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._user = None
        self._hub_domain = None
        self._scopes = None
        self._scope_to_scope_group_pks = None
        self._hub_id = None
        self._app_id = None
        self._expires_in = None
        self._user_id = None
        self._token_type = None
        self.discriminator = None

        self.token = token
        if user is not None:
            self.user = user
        if hub_domain is not None:
            self.hub_domain = hub_domain
        self.scopes = scopes
        self.scope_to_scope_group_pks = scope_to_scope_group_pks
        self.hub_id = hub_id
        self.app_id = app_id
        self.expires_in = expires_in
        self.user_id = user_id
        self.token_type = token_type

    @property
    def token(self):
        """Gets the token of this AccessTokenInfoResponse.  # noqa: E501


        :return: The token of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AccessTokenInfoResponse.


        :param token: The token of this AccessTokenInfoResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def user(self):
        """Gets the user of this AccessTokenInfoResponse.  # noqa: E501


        :return: The user of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AccessTokenInfoResponse.


        :param user: The user of this AccessTokenInfoResponse.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def hub_domain(self):
        """Gets the hub_domain of this AccessTokenInfoResponse.  # noqa: E501


        :return: The hub_domain of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._hub_domain

    @hub_domain.setter
    def hub_domain(self, hub_domain):
        """Sets the hub_domain of this AccessTokenInfoResponse.


        :param hub_domain: The hub_domain of this AccessTokenInfoResponse.  # noqa: E501
        :type: str
        """

        self._hub_domain = hub_domain

    @property
    def scopes(self):
        """Gets the scopes of this AccessTokenInfoResponse.  # noqa: E501


        :return: The scopes of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this AccessTokenInfoResponse.


        :param scopes: The scopes of this AccessTokenInfoResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and scopes is None:  # noqa: E501
            raise ValueError("Invalid value for `scopes`, must not be `None`")  # noqa: E501

        self._scopes = scopes

    @property
    def scope_to_scope_group_pks(self):
        """Gets the scope_to_scope_group_pks of this AccessTokenInfoResponse.  # noqa: E501


        :return: The scope_to_scope_group_pks of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._scope_to_scope_group_pks

    @scope_to_scope_group_pks.setter
    def scope_to_scope_group_pks(self, scope_to_scope_group_pks):
        """Sets the scope_to_scope_group_pks of this AccessTokenInfoResponse.


        :param scope_to_scope_group_pks: The scope_to_scope_group_pks of this AccessTokenInfoResponse.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and scope_to_scope_group_pks is None:  # noqa: E501
            raise ValueError("Invalid value for `scope_to_scope_group_pks`, must not be `None`")  # noqa: E501

        self._scope_to_scope_group_pks = scope_to_scope_group_pks

    @property
    def hub_id(self):
        """Gets the hub_id of this AccessTokenInfoResponse.  # noqa: E501


        :return: The hub_id of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._hub_id

    @hub_id.setter
    def hub_id(self, hub_id):
        """Sets the hub_id of this AccessTokenInfoResponse.


        :param hub_id: The hub_id of this AccessTokenInfoResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hub_id is None:  # noqa: E501
            raise ValueError("Invalid value for `hub_id`, must not be `None`")  # noqa: E501

        self._hub_id = hub_id

    @property
    def app_id(self):
        """Gets the app_id of this AccessTokenInfoResponse.  # noqa: E501


        :return: The app_id of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AccessTokenInfoResponse.


        :param app_id: The app_id of this AccessTokenInfoResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def expires_in(self):
        """Gets the expires_in of this AccessTokenInfoResponse.  # noqa: E501


        :return: The expires_in of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this AccessTokenInfoResponse.


        :param expires_in: The expires_in of this AccessTokenInfoResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expires_in is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

    @property
    def user_id(self):
        """Gets the user_id of this AccessTokenInfoResponse.  # noqa: E501


        :return: The user_id of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AccessTokenInfoResponse.


        :param user_id: The user_id of this AccessTokenInfoResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def token_type(self):
        """Gets the token_type of this AccessTokenInfoResponse.  # noqa: E501


        :return: The token_type of this AccessTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this AccessTokenInfoResponse.


        :param token_type: The token_type of this AccessTokenInfoResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token_type is None:  # noqa: E501
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

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
        if not isinstance(other, AccessTokenInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessTokenInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
