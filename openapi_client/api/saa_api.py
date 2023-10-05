# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from datetime import date

from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_settlement_settlement_message_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SAAApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def balancing_settlement_messages_settlement_date_get(self, settlement_date : Annotated[date, Field(..., description="The settlement date to filter. This must be in the format yyyy-MM-dd.")], format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse:  # noqa: E501
        """Settlement Messages by settlement date (PREVIEW)  # noqa: E501

        ⚠ This is a preview feature. It currently returns empty or incomplete data, as Insights does not yet have full access to this data.    Returns settlement messages generated by the SAA for a given settlement day, relating to the data  for a settlement run.                For each settlement period within the range, only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_settlement_messages_settlement_date_get(settlement_date, format, async_req=True)
        >>> result = thread.get()

        :param settlement_date: The settlement date to filter. This must be in the format yyyy-MM-dd. (required)
        :type settlement_date: date
        :param format: Response data format. Use json/xml to include metadata.
        :type format: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the balancing_settlement_messages_settlement_date_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.balancing_settlement_messages_settlement_date_get_with_http_info(settlement_date, format, **kwargs)  # noqa: E501

    @validate_arguments
    def balancing_settlement_messages_settlement_date_get_with_http_info(self, settlement_date : Annotated[date, Field(..., description="The settlement date to filter. This must be in the format yyyy-MM-dd.")], format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Settlement Messages by settlement date (PREVIEW)  # noqa: E501

        ⚠ This is a preview feature. It currently returns empty or incomplete data, as Insights does not yet have full access to this data.    Returns settlement messages generated by the SAA for a given settlement day, relating to the data  for a settlement run.                For each settlement period within the range, only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_settlement_messages_settlement_date_get_with_http_info(settlement_date, format, async_req=True)
        >>> result = thread.get()

        :param settlement_date: The settlement date to filter. This must be in the format yyyy-MM-dd. (required)
        :type settlement_date: date
        :param format: Response data format. Use json/xml to include metadata.
        :type format: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'settlement_date',
            'format'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method balancing_settlement_messages_settlement_date_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['settlement_date']:
            _path_params['settlementDate'] = _params['settlement_date']


        # process the query parameters
        _query_params = []
        if _params.get('format') is not None:  # noqa: E501
            _query_params.append(('format', _params['format']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/balancing/settlement/messages/{settlementDate}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def balancing_settlement_messages_settlement_date_settlement_period_get(self, settlement_period : Annotated[StrictInt, Field(..., description="The settlement period to filter. This should be an integer from 1-50 inclusive.")], settlement_date : Annotated[date, Field(..., description="The settlement date to filter. This must be in the format yyyy-MM-dd.")], format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse:  # noqa: E501
        """Settlement Messages by settlement date and period (PREVIEW)  # noqa: E501

        ⚠ This is a preview feature. It currently returns empty or incomplete data, as Insights does not yet have full access to this data.    Returns settlement messages generated by the SAA for a given settlement period, relating to the data  for a settlement run.                Only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_settlement_messages_settlement_date_settlement_period_get(settlement_period, settlement_date, format, async_req=True)
        >>> result = thread.get()

        :param settlement_period: The settlement period to filter. This should be an integer from 1-50 inclusive. (required)
        :type settlement_period: int
        :param settlement_date: The settlement date to filter. This must be in the format yyyy-MM-dd. (required)
        :type settlement_date: date
        :param format: Response data format. Use json/xml to include metadata.
        :type format: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the balancing_settlement_messages_settlement_date_settlement_period_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.balancing_settlement_messages_settlement_date_settlement_period_get_with_http_info(settlement_period, settlement_date, format, **kwargs)  # noqa: E501

    @validate_arguments
    def balancing_settlement_messages_settlement_date_settlement_period_get_with_http_info(self, settlement_period : Annotated[StrictInt, Field(..., description="The settlement period to filter. This should be an integer from 1-50 inclusive.")], settlement_date : Annotated[date, Field(..., description="The settlement date to filter. This must be in the format yyyy-MM-dd.")], format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Settlement Messages by settlement date and period (PREVIEW)  # noqa: E501

        ⚠ This is a preview feature. It currently returns empty or incomplete data, as Insights does not yet have full access to this data.    Returns settlement messages generated by the SAA for a given settlement period, relating to the data  for a settlement run.                Only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_settlement_messages_settlement_date_settlement_period_get_with_http_info(settlement_period, settlement_date, format, async_req=True)
        >>> result = thread.get()

        :param settlement_period: The settlement period to filter. This should be an integer from 1-50 inclusive. (required)
        :type settlement_period: int
        :param settlement_date: The settlement date to filter. This must be in the format yyyy-MM-dd. (required)
        :type settlement_date: date
        :param format: Response data format. Use json/xml to include metadata.
        :type format: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'settlement_period',
            'settlement_date',
            'format'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method balancing_settlement_messages_settlement_date_settlement_period_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['settlement_period']:
            _path_params['settlementPeriod'] = _params['settlement_period']

        if _params['settlement_date']:
            _path_params['settlementDate'] = _params['settlement_date']


        # process the query parameters
        _query_params = []
        if _params.get('format') is not None:  # noqa: E501
            _query_params.append(('format', _params['format']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/balancing/settlement/messages/{settlementDate}/{settlementPeriod}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
