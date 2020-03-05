# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SchemaApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def bulk_fetch_event_meta_info(self, **kwargs):
        """
        Get Event meta Information
        Bulk fetch of event meta info. Max batch size is 1000.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bulk_fetch_event_meta_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: EventMetaInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.bulk_fetch_event_meta_info_with_http_info(**kwargs)
        else:
            (data) = self.bulk_fetch_event_meta_info_with_http_info(**kwargs)
            return data

    def bulk_fetch_event_meta_info_with_http_info(self, **kwargs):
        """
        Get Event meta Information
        Bulk fetch of event meta info. Max batch size is 1000.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bulk_fetch_event_meta_info_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: EventMetaInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_fetch_event_meta_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/schema/problems', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EventMetaInfoResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_metrics_schema(self, entity_type, **kwargs):
        """
        Get metrics schema for an entity type
        Get details of metrics available for entity type
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metrics_schema(entity_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_type: entity type (required)
        :return: EntityMetricsSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_metrics_schema_with_http_info(entity_type, **kwargs)
        else:
            (data) = self.get_metrics_schema_with_http_info(entity_type, **kwargs)
            return data

    def get_metrics_schema_with_http_info(self, entity_type, **kwargs):
        """
        Get metrics schema for an entity type
        Get details of metrics available for entity type
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metrics_schema_with_http_info(entity_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_type: entity type (required)
        :return: EntityMetricsSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metrics_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params) or (params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_metrics_schema`")


        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entity-type'] = params['entity_type']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/schema/{entity-type}/metrics', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EntityMetricsSchema',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
