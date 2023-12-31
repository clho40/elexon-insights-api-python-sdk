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

from pydantic import Field, StrictInt, StrictStr, conlist

from typing import Optional

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_bid_offer_acceptances_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class BidOfferAcceptancesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def balancing_acceptances_all_get(self, settlement_date : Annotated[datetime, Field(..., description="The settlement date or datetime for the filter.")], settlement_period : Annotated[Optional[StrictInt], Field(description="The settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, bm_unit : Annotated[Optional[conlist(StrictStr)], Field(description="The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned.")] = None, format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse:  # noqa: E501
        """Bid Offer Acceptances Market-wide  # noqa: E501

        This endpoint provides the bid offer acceptance data (BOAL) for multiple requested BMUs or all BMUs.  It returns the data valid for a single settlement period.                The settlement period to query can be specified as a date and settlement period, or as a datetime  which will resolve to the settlement period that time falls within.    All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Note: When a settlementPeriod is supplied, the settlementDate parameter is treated as a Date only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.    Some examples of date parameter combinations are shown below.                Filtering by settlement date and period:                    /balancing/acceptances/all?settlementDate=2023-01-24&settlementPeriod=39                Filtering by datetime:                    /balancing/acceptances/all?settlementDate=2023-01-24T19:00Z  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_acceptances_all_get(settlement_date, settlement_period, bm_unit, format, async_req=True)
        >>> result = thread.get()

        :param settlement_date: The settlement date or datetime for the filter. (required)
        :type settlement_date: datetime
        :param settlement_period: The settlement period for the filter. This should be an integer from 1-50 inclusive.
        :type settlement_period: int
        :param bm_unit: The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned.
        :type bm_unit: List[str]
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
        :rtype: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the balancing_acceptances_all_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.balancing_acceptances_all_get_with_http_info(settlement_date, settlement_period, bm_unit, format, **kwargs)  # noqa: E501

    @validate_arguments
    def balancing_acceptances_all_get_with_http_info(self, settlement_date : Annotated[datetime, Field(..., description="The settlement date or datetime for the filter.")], settlement_period : Annotated[Optional[StrictInt], Field(description="The settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, bm_unit : Annotated[Optional[conlist(StrictStr)], Field(description="The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned.")] = None, format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Bid Offer Acceptances Market-wide  # noqa: E501

        This endpoint provides the bid offer acceptance data (BOAL) for multiple requested BMUs or all BMUs.  It returns the data valid for a single settlement period.                The settlement period to query can be specified as a date and settlement period, or as a datetime  which will resolve to the settlement period that time falls within.    All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Note: When a settlementPeriod is supplied, the settlementDate parameter is treated as a Date only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.    Some examples of date parameter combinations are shown below.                Filtering by settlement date and period:                    /balancing/acceptances/all?settlementDate=2023-01-24&settlementPeriod=39                Filtering by datetime:                    /balancing/acceptances/all?settlementDate=2023-01-24T19:00Z  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_acceptances_all_get_with_http_info(settlement_date, settlement_period, bm_unit, format, async_req=True)
        >>> result = thread.get()

        :param settlement_date: The settlement date or datetime for the filter. (required)
        :type settlement_date: datetime
        :param settlement_period: The settlement period for the filter. This should be an integer from 1-50 inclusive.
        :type settlement_period: int
        :param bm_unit: The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned.
        :type bm_unit: List[str]
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
        :rtype: tuple(InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'settlement_date',
            'settlement_period',
            'bm_unit',
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
                    " to method balancing_acceptances_all_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('settlement_date') is not None:  # noqa: E501
            if isinstance(_params['settlement_date'], datetime):
                _query_params.append(('settlementDate', _params['settlement_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('settlementDate', _params['settlement_date']))

        if _params.get('settlement_period') is not None:  # noqa: E501
            _query_params.append(('settlementPeriod', _params['settlement_period']))

        if _params.get('bm_unit') is not None:  # noqa: E501
            _query_params.append(('bmUnit', _params['bm_unit']))
            _collection_formats['bmUnit'] = 'multi'

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
            '200': "InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/balancing/acceptances/all', 'GET',
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
    def balancing_acceptances_get(self, bm_unit : Annotated[StrictStr, Field(..., description="The BM Unit to query.")], var_from : Annotated[datetime, Field(..., description="The \"from\" start time or settlement date for the filter.")], to : Annotated[datetime, Field(..., description="The \"to\" start time or settlement date for the filter.")], settlement_period_from : Annotated[Optional[StrictInt], Field(description="The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, settlement_period_to : Annotated[Optional[StrictInt], Field(description="The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse:  # noqa: E501
        """Bid Offer Acceptances Per-BMU  # noqa: E501

        This endpoint provides the bid offer acceptance data (BOAL) for a requested BMU.                By default, the from and to parameters filter the data by start time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of start time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_acceptances_get(bm_unit, var_from, to, settlement_period_from, settlement_period_to, format, async_req=True)
        >>> result = thread.get()

        :param bm_unit: The BM Unit to query. (required)
        :type bm_unit: str
        :param var_from: The \"from\" start time or settlement date for the filter. (required)
        :type var_from: datetime
        :param to: The \"to\" start time or settlement date for the filter. (required)
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
        :rtype: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the balancing_acceptances_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.balancing_acceptances_get_with_http_info(bm_unit, var_from, to, settlement_period_from, settlement_period_to, format, **kwargs)  # noqa: E501

    @validate_arguments
    def balancing_acceptances_get_with_http_info(self, bm_unit : Annotated[StrictStr, Field(..., description="The BM Unit to query.")], var_from : Annotated[datetime, Field(..., description="The \"from\" start time or settlement date for the filter.")], to : Annotated[datetime, Field(..., description="The \"to\" start time or settlement date for the filter.")], settlement_period_from : Annotated[Optional[StrictInt], Field(description="The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, settlement_period_to : Annotated[Optional[StrictInt], Field(description="The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.")] = None, format : Annotated[Optional[StrictStr], Field(description="Response data format. Use json/xml to include metadata.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Bid Offer Acceptances Per-BMU  # noqa: E501

        This endpoint provides the bid offer acceptance data (BOAL) for a requested BMU.                By default, the from and to parameters filter the data by start time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of start time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balancing_acceptances_get_with_http_info(bm_unit, var_from, to, settlement_period_from, settlement_period_to, format, async_req=True)
        >>> result = thread.get()

        :param bm_unit: The BM Unit to query. (required)
        :type bm_unit: str
        :param var_from: The \"from\" start time or settlement date for the filter. (required)
        :type var_from: datetime
        :param to: The \"to\" start time or settlement date for the filter. (required)
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
        :rtype: tuple(InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'bm_unit',
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
                    " to method balancing_acceptances_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('bm_unit') is not None:  # noqa: E501
            _query_params.append(('bmUnit', _params['bm_unit']))

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
            '200': "InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/balancing/acceptances', 'GET',
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
