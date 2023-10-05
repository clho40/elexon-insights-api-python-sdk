# openapi_client.BalancingServicesAdjustmentNetApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_nonbm_netbsad_events_get**](BalancingServicesAdjustmentNetApi.md#balancing_nonbm_netbsad_events_get) | **GET** /balancing/nonbm/netbsad/events | Net Balancing Services Adjustment (NETBSAD) events
[**balancing_nonbm_netbsad_get**](BalancingServicesAdjustmentNetApi.md#balancing_nonbm_netbsad_get) | **GET** /balancing/nonbm/netbsad | Net Balancing Services Adjustment (NETBSAD) time series


# **balancing_nonbm_netbsad_events_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse balancing_nonbm_netbsad_events_get(count, before=before, settlement_period_before=settlement_period_before, format=format)

Net Balancing Services Adjustment (NETBSAD) events

This endpoint provides data about the start of NGESO Net Balancing Services Adjustment (NETBSAD) events.  An event is a point in time where one of the NETBSAD values has changed from 0 to a value.  Each event details the start time of the event and the NETBSAD values associated with the start of the event.                By default, the before parameter filters the data by start time. If the settlementPeriodBefore parameter is  provided, the before parameter instead filters on settlement date, allowing for searching by start time or  settlement date & settlement period.  Note: When filtering via settlement date, before is treated as a Date only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering latest 3 events:                    /balancing/nonbm/netbsad/events?count=3                Filtering latest 3 events before start time:                    /balancing/nonbm/netbsad/events?before=2022-08-01T00:00Z&count=3                Filtering latest 3 events before settlement date and settlement period:                    /balancing/nonbm/netbsad/events?before=2022-08-01T00:00Z&settlementPeriodBefore=48&count=3

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_net_balancing_services_adjustment_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://data.elexon.co.uk/bmrs/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://data.elexon.co.uk/bmrs/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BalancingServicesAdjustmentNetApi(api_client)
    count = 3 # int | The number of events to return.
    before = '2013-10-20T19:20:30+01:00' # datetime | If specified, filters events to those with a start time before or at the date, or a settlement date before the date if  settlementPeriodBefore is also specified.  If omitted, latest events are returned. (optional)
    settlement_period_before = 56 # int | Filters events to those with a settlement period before or at the value.  Before parameter must be specified if this is specified. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Net Balancing Services Adjustment (NETBSAD) events
        api_response = api_instance.balancing_nonbm_netbsad_events_get(count, before=before, settlement_period_before=settlement_period_before, format=format)
        print("The response of BalancingServicesAdjustmentNetApi->balancing_nonbm_netbsad_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingServicesAdjustmentNetApi->balancing_nonbm_netbsad_events_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| The number of events to return. | 
 **before** | **datetime**| If specified, filters events to those with a start time before or at the date, or a settlement date before the date if  settlementPeriodBefore is also specified.  If omitted, latest events are returned. | [optional] 
 **settlement_period_before** | **int**| Filters events to those with a settlement period before or at the value.  Before parameter must be specified if this is specified. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balancing_nonbm_netbsad_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse balancing_nonbm_netbsad_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, include_zero=include_zero, format=format)

Net Balancing Services Adjustment (NETBSAD) time series

This endpoint provides data about the Net Balancing Services Adjustment (NETBSAD). Each  entry in the time series contains the NETBSAD values for that settlement period.                By default, the from and to parameters filter the data by time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/nonbm/netbsad?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/nonbm/netbsad?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/nonbm/netbsad?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/nonbm/netbsad?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_net_balancing_services_adjustment_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://data.elexon.co.uk/bmrs/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://data.elexon.co.uk/bmrs/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BalancingServicesAdjustmentNetApi(api_client)
    var_from = '2022-06-01T00:00Z' # datetime | The \"from\" start time or settlement date for the filter.
    to = '2022-07-01T00:00Z' # datetime | The \"to\" start time or settlement date for the filter.
    settlement_period_from = 56 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    settlement_period_to = 56 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    include_zero = false # bool | Include data points with a generation of zero. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Net Balancing Services Adjustment (NETBSAD) time series
        api_response = api_instance.balancing_nonbm_netbsad_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, include_zero=include_zero, format=format)
        print("The response of BalancingServicesAdjustmentNetApi->balancing_nonbm_netbsad_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingServicesAdjustmentNetApi->balancing_nonbm_netbsad_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **include_zero** | **bool**| Include data points with a generation of zero. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

