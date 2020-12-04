# coding: utf-8

"""
    Associations

    Associations define the relationships between objects in HubSpot. These endpoints allow you to create, read, and remove associations.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.associations.api_client import ApiClient
from hubspot.crm.associations.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class BatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """Archive a batch of associations  # noqa: E501

        Remove the associations between all pairs of objects identified in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociation batch_input_public_association:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.archive_with_http_info(from_object_type, to_object_type, **kwargs)  # noqa: E501

    def archive_with_http_info(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """Archive a batch of associations  # noqa: E501

        Remove the associations between all pairs of objects identified in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociation batch_input_public_association:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'from_object_type',
            'to_object_type',
            'batch_input_public_association'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ('from_object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['from_object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ('to_object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['to_object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'from_object_type' in local_var_params:
            path_params['fromObjectType'] = local_var_params['from_object_type']  # noqa: E501
        if 'to_object_type' in local_var_params:
            path_params['toObjectType'] = local_var_params['to_object_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_input_public_association' in local_var_params:
            body_params = local_var_params['batch_input_public_association']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/archive', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """Create a batch of associations  # noqa: E501

        Associate all pairs of objects identified in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociation batch_input_public_association:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponsePublicAssociation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(from_object_type, to_object_type, **kwargs)  # noqa: E501

    def create_with_http_info(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """Create a batch of associations  # noqa: E501

        Associate all pairs of objects identified in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociation batch_input_public_association:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponsePublicAssociation, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'from_object_type',
            'to_object_type',
            'batch_input_public_association'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ('from_object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['from_object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ('to_object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['to_object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'from_object_type' in local_var_params:
            path_params['fromObjectType'] = local_var_params['from_object_type']  # noqa: E501
        if 'to_object_type' in local_var_params:
            path_params['toObjectType'] = local_var_params['to_object_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_input_public_association' in local_var_params:
            body_params = local_var_params['batch_input_public_association']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchResponsePublicAssociation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """Read a batch of associations  # noqa: E501

        Get the IDs of all `{toObjectType}` objects associated with those specified in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicObjectId batch_input_public_object_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponsePublicAssociationMulti
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(from_object_type, to_object_type, **kwargs)  # noqa: E501

    def read_with_http_info(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """Read a batch of associations  # noqa: E501

        Get the IDs of all `{toObjectType}` objects associated with those specified in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicObjectId batch_input_public_object_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponsePublicAssociationMulti, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'from_object_type',
            'to_object_type',
            'batch_input_public_object_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ('from_object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['from_object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `read`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ('to_object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['to_object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'from_object_type' in local_var_params:
            path_params['fromObjectType'] = local_var_params['from_object_type']  # noqa: E501
        if 'to_object_type' in local_var_params:
            path_params['toObjectType'] = local_var_params['to_object_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_input_public_object_id' in local_var_params:
            body_params = local_var_params['batch_input_public_object_id']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/read', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchResponsePublicAssociationMulti',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
