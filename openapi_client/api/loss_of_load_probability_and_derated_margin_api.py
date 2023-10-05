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
from datetime import datetime

from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LossOfLoadProbabilityAndDeratedMarginApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def lolpdrm_forecast_evolution_get(self, var_from : datetime, to : datetime, settlement_period_from : Annotated[Optional[StrictInt], Field(description="The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, settlement_period_to : Annotated[Optional[StrictInt], Field(description="The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse:  # noqa: E501
        """Loss of Load Probability and De-rated Margin forecasts per settlement period  # noqa: E501

        This endpoint provides the 1h, 2h, 4h, 8h and 12h+ Loss of Load Probability and De-rated Margin forecasts  for each settlement period over a requested time range.                For each forecast horizon at 1, 2, 4 or 8 hours, the returned value is the forecast received that number of hours  before the start of the settlement period.                For the forecast horizon of 12h, the returned value is the most recent forecast received 12 or more hours  before the start of the settlement period. That is, if the most recent forecast was published today at 00:00,  - for 11:30 today, the 12h forecast is the one published yesterday at 23:30 (12h before)  - for 12:00 today, the 12h forecast is the one published today at 00:00 (12h before)  - for 12:30 today, the 12h forecast is the one published today at 00:00 (the latest published)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lolpdrm_forecast_evolution_get(var_from, to, settlement_period_from, settlement_period_to, format, async_req=True)
        >>> result = thread.get()

        :param var_from: (required)
        :type var_from: datetime
        :param to: (required)
        :type to: datetime
        :param settlement_period_from: The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :type settlement_period_from: int
        :param settlement_period_to: The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :type settlement_period_to: int
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
        :rtype: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the lolpdrm_forecast_evolution_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.lolpdrm_forecast_evolution_get_with_http_info(var_from, to, settlement_period_from, settlement_period_to, format, **kwargs)  # noqa: E501

    @validate_arguments
    def lolpdrm_forecast_evolution_get_with_http_info(self, var_from : datetime, to : datetime, settlement_period_from : Annotated[Optional[StrictInt], Field(description="The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, settlement_period_to : Annotated[Optional[StrictInt], Field(description="The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Loss of Load Probability and De-rated Margin forecasts per settlement period  # noqa: E501

        This endpoint provides the 1h, 2h, 4h, 8h and 12h+ Loss of Load Probability and De-rated Margin forecasts  for each settlement period over a requested time range.                For each forecast horizon at 1, 2, 4 or 8 hours, the returned value is the forecast received that number of hours  before the start of the settlement period.                For the forecast horizon of 12h, the returned value is the most recent forecast received 12 or more hours  before the start of the settlement period. That is, if the most recent forecast was published today at 00:00,  - for 11:30 today, the 12h forecast is the one published yesterday at 23:30 (12h before)  - for 12:00 today, the 12h forecast is the one published today at 00:00 (12h before)  - for 12:30 today, the 12h forecast is the one published today at 00:00 (the latest published)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lolpdrm_forecast_evolution_get_with_http_info(var_from, to, settlement_period_from, settlement_period_to, format, async_req=True)
        >>> result = thread.get()

        :param var_from: (required)
        :type var_from: datetime
        :param to: (required)
        :type to: datetime
        :param settlement_period_from: The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :type settlement_period_from: int
        :param settlement_period_to: The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :type settlement_period_to: int
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
        :rtype: tuple(InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'var_from',
            'to',
            'settlement_period_from',
            'settlement_period_to',
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
                    " to method lolpdrm_forecast_evolution_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('var_from') is not None:  # noqa: E501
            if isinstance(_params['var_from'], datetime):
                _query_params.append(('from', _params['var_from'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            if isinstance(_params['to'], datetime):
                _query_params.append(('to', _params['to'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('to', _params['to']))

        if _params.get('settlement_period_from') is not None:  # noqa: E501
            _query_params.append(('settlementPeriodFrom', _params['settlement_period_from']))

        if _params.get('settlement_period_to') is not None:  # noqa: E501
            _query_params.append(('settlementPeriodTo', _params['settlement_period_to']))

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
            '200': "InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/lolpdrm/forecast/evolution', 'GET',
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
