# openapi_client.BalancingServicesAdjustmentDisaggregatedApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_nonbm_disbsad_details_get**](BalancingServicesAdjustmentDisaggregatedApi.md#balancing_nonbm_disbsad_details_get) | **GET** /balancing/nonbm/disbsad/details | Disaggregated balancing services adjustment (DISBSAD) per settlement period
[**balancing_nonbm_disbsad_summary_get**](BalancingServicesAdjustmentDisaggregatedApi.md#balancing_nonbm_disbsad_summary_get) | **GET** /balancing/nonbm/disbsad/summary | Disaggregated balancing services adjustment (DISBSAD) time series


# **balancing_nonbm_disbsad_details_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse balancing_nonbm_disbsad_details_get(settlement_date, settlement_period, format=format)

Disaggregated balancing services adjustment (DISBSAD) per settlement period

This endpoint provides disaggregated balancing services adjustment data for a single settlement period. The  response includes all the buying and selling actions that occurred during that settlement period.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse
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
    api_instance = openapi_client.BalancingServicesAdjustmentDisaggregatedApi(api_client)
    settlement_date = '2022-10-26' # date | The settlement date to query.
    settlement_period = 3 # int | The settlement period to query. This should be an integer from 1-50 inclusive.
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Disaggregated balancing services adjustment (DISBSAD) per settlement period
        api_response = api_instance.balancing_nonbm_disbsad_details_get(settlement_date, settlement_period, format=format)
        print("The response of BalancingServicesAdjustmentDisaggregatedApi->balancing_nonbm_disbsad_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingServicesAdjustmentDisaggregatedApi->balancing_nonbm_disbsad_details_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| The settlement date to query. | 
 **settlement_period** | **int**| The settlement period to query. This should be an integer from 1-50 inclusive. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.md)

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

# **balancing_nonbm_disbsad_summary_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse balancing_nonbm_disbsad_summary_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Disaggregated balancing services adjustment (DISBSAD) time series

This endpoint provides disaggregated balancing services adjustment data batched by settlement period. Each  batch in the time series contains a summary of all records for that settlement period, detailing the number of  buy and sell actions, price information and volume information.    By default, the from and to parameters filter the data by start time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of start time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/nonbm/disbsad/summary?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/nonbm/disbsad/summary?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/nonbm/disbsad/summary?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/nonbm/disbsad/summary?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse
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
    api_instance = openapi_client.BalancingServicesAdjustmentDisaggregatedApi(api_client)
    var_from = '2022-09-20T00:00Z' # datetime | The \"from\" start time or settlement date for the filter.
    to = '2022-09-27T00:00Z' # datetime | The \"to\" start time or settlement date for the filter.
    settlement_period_from = 56 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    settlement_period_to = 56 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Disaggregated balancing services adjustment (DISBSAD) time series
        api_response = api_instance.balancing_nonbm_disbsad_summary_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of BalancingServicesAdjustmentDisaggregatedApi->balancing_nonbm_disbsad_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingServicesAdjustmentDisaggregatedApi->balancing_nonbm_disbsad_summary_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse.md)

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

