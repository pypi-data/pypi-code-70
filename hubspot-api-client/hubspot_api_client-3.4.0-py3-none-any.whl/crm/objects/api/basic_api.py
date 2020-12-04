# coding: utf-8

"""
    CRM Objects

    CRM objects such as companies, contacts, deals, line items, products, tickets, and quotes are standard objects in HubSpot’s CRM. These core building blocks support custom properties, store critical information, and play a central role in the HubSpot application.  ## Supported Object Types  This API provides access to collections of CRM objects, which return a map of property names to values. Each object type has its own set of default properties, which can be found by exploring the [CRM Object Properties API](https://developers.hubspot.com/docs/methods/crm-properties/crm-properties-overview).  |Object Type |Properties returned by default | |--|--| | `companies` | `name`, `domain` | | `contacts` | `firstname`, `lastname`, `email` | | `deals` | `dealname`, `amount`, `closedate`, `pipeline`, `dealstage` | | `products` | `name`, `description`, `price` | | `tickets` | `content`, `hs_pipeline`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_priority`, `subject` |  Find a list of all properties for an object type using the [CRM Object Properties](https://developers.hubspot.com/docs/methods/crm-properties/get-properties) API. e.g. `GET https://api.hubapi.com/properties/v2/companies/properties`. Change the properties returned in the response using the `properties` array in the request body.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.objects.api_client import ApiClient
from hubspot.crm.objects.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class BasicApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, object_type, object_id, **kwargs):  # noqa: E501
        """Archive  # noqa: E501

        Move an Object identified by `{objectId}` to the recycling bin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(object_type, object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str object_id: (required)
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
        return self.archive_with_http_info(object_type, object_id, **kwargs)  # noqa: E501

    def archive_with_http_info(self, object_type, object_id, **kwargs):  # noqa: E501
        """Archive  # noqa: E501

        Move an Object identified by `{objectId}` to the recycling bin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(object_type, object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str object_id: (required)
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
            'object_type',
            'object_id'
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
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and ('object_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_id` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501
        if 'object_id' in local_var_params:
            path_params['objectId'] = local_var_params['object_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/objects/{objectType}/{objectId}', 'DELETE',
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

    def create(self, object_type, simple_public_object_input, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Create a CRM object with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard objects is provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(object_type, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param SimplePublicObjectInput simple_public_object_input: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(object_type, simple_public_object_input, **kwargs)  # noqa: E501

    def create_with_http_info(self, object_type, simple_public_object_input, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Create a CRM object with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard objects is provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(object_type, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param SimplePublicObjectInput simple_public_object_input: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'object_type',
            'simple_public_object_input'
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
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'simple_public_object_input' is set
        if self.api_client.client_side_validation and ('simple_public_object_input' not in local_var_params or  # noqa: E501
                                                        local_var_params['simple_public_object_input'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `simple_public_object_input` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'simple_public_object_input' in local_var_params:
            body_params = local_var_params['simple_public_object_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/objects/{objectType}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimplePublicObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_by_id(self, object_type, object_id, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{objectId}`. `{objectId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(object_type, object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str object_id: (required)
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
        :param bool archived: Whether to return only results that have been archived.
        :param str id_property: The name of a property whose values are unique for this object type
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_by_id_with_http_info(object_type, object_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, object_type, object_id, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{objectId}`. `{objectId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(object_type, object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str object_id: (required)
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
        :param bool archived: Whether to return only results that have been archived.
        :param str id_property: The name of a property whose values are unique for this object type
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'object_type',
            'object_id',
            'properties',
            'associations',
            'paginate_associations',
            'archived',
            'id_property'
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
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `get_by_id`")  # noqa: E501
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and ('object_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501
        if 'object_id' in local_var_params:
            path_params['objectId'] = local_var_params['object_id']  # noqa: E501

        query_params = []
        if 'properties' in local_var_params and local_var_params['properties'] is not None:  # noqa: E501
            query_params.append(('properties', local_var_params['properties']))  # noqa: E501
            collection_formats['properties'] = 'multi'  # noqa: E501
        if 'associations' in local_var_params and local_var_params['associations'] is not None:  # noqa: E501
            query_params.append(('associations', local_var_params['associations']))  # noqa: E501
            collection_formats['associations'] = 'multi'  # noqa: E501
        if 'paginate_associations' in local_var_params and local_var_params['paginate_associations'] is not None:  # noqa: E501
            query_params.append(('paginateAssociations', local_var_params['paginate_associations']))  # noqa: E501
        if 'archived' in local_var_params and local_var_params['archived'] is not None:  # noqa: E501
            query_params.append(('archived', local_var_params['archived']))  # noqa: E501
        if 'id_property' in local_var_params and local_var_params['id_property'] is not None:  # noqa: E501
            query_params.append(('idProperty', local_var_params['id_property']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/objects/{objectType}/{objectId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimplePublicObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_page(self, object_type, **kwargs):  # noqa: E501
        """List  # noqa: E501

        Read a page of objects. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param int limit: The maximum number of results to display per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
        :param bool archived: Whether to return only results that have been archived.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseSimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_page_with_http_info(object_type, **kwargs)  # noqa: E501

    def get_page_with_http_info(self, object_type, **kwargs):  # noqa: E501
        """List  # noqa: E501

        Read a page of objects. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_with_http_info(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param int limit: The maximum number of results to display per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
        :param bool archived: Whether to return only results that have been archived.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'object_type',
            'limit',
            'after',
            'properties',
            'associations',
            'paginate_associations',
            'archived'
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
                    " to method get_page" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `get_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'after' in local_var_params and local_var_params['after'] is not None:  # noqa: E501
            query_params.append(('after', local_var_params['after']))  # noqa: E501
        if 'properties' in local_var_params and local_var_params['properties'] is not None:  # noqa: E501
            query_params.append(('properties', local_var_params['properties']))  # noqa: E501
            collection_formats['properties'] = 'multi'  # noqa: E501
        if 'associations' in local_var_params and local_var_params['associations'] is not None:  # noqa: E501
            query_params.append(('associations', local_var_params['associations']))  # noqa: E501
            collection_formats['associations'] = 'multi'  # noqa: E501
        if 'paginate_associations' in local_var_params and local_var_params['paginate_associations'] is not None:  # noqa: E501
            query_params.append(('paginateAssociations', local_var_params['paginate_associations']))  # noqa: E501
        if 'archived' in local_var_params and local_var_params['archived'] is not None:  # noqa: E501
            query_params.append(('archived', local_var_params['archived']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/objects/{objectType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionResponseSimplePublicObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, object_type, object_id, simple_public_object_input, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        Perform a partial update of an Object identified by `{objectId}`. Provided property values will be overwritten. Read-only and non-existent properties will be ignored. Properties values can be cleared by passing an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(object_type, object_id, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str object_id: (required)
        :param SimplePublicObjectInput simple_public_object_input: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_with_http_info(object_type, object_id, simple_public_object_input, **kwargs)  # noqa: E501

    def update_with_http_info(self, object_type, object_id, simple_public_object_input, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        Perform a partial update of an Object identified by `{objectId}`. Provided property values will be overwritten. Read-only and non-existent properties will be ignored. Properties values can be cleared by passing an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(object_type, object_id, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str object_id: (required)
        :param SimplePublicObjectInput simple_public_object_input: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'object_type',
            'object_id',
            'simple_public_object_input'
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
                    " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `update`")  # noqa: E501
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and ('object_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_id` when calling `update`")  # noqa: E501
        # verify the required parameter 'simple_public_object_input' is set
        if self.api_client.client_side_validation and ('simple_public_object_input' not in local_var_params or  # noqa: E501
                                                        local_var_params['simple_public_object_input'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `simple_public_object_input` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501
        if 'object_id' in local_var_params:
            path_params['objectId'] = local_var_params['object_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'simple_public_object_input' in local_var_params:
            body_params = local_var_params['simple_public_object_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/objects/{objectType}/{objectId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimplePublicObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
