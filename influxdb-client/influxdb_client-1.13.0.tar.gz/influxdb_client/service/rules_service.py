# coding: utf-8

"""
Influx API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 0.1.0
Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from influxdb_client.api_client import ApiClient


class RulesService(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """RulesService - a operation defined in OpenAPI."""
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_notification_rules_id_query(self, rule_id, **kwargs):  # noqa: E501,D401,D403
        """Get a notification rule query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rules_id_query(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The notification rule ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notification_rules_id_query_with_http_info(rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notification_rules_id_query_with_http_info(rule_id, **kwargs)  # noqa: E501
            return data

    def get_notification_rules_id_query_with_http_info(self, rule_id, **kwargs):  # noqa: E501,D401,D403
        """Get a notification rule query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rules_id_query_with_http_info(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The notification rule ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['rule_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notification_rules_id_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in local_var_params or
                local_var_params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `get_notification_rules_id_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['ruleID'] = local_var_params['rule_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/notificationRules/{ruleID}/query', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FluxResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)
