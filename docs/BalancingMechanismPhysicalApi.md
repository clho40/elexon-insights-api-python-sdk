# openapi_client.BalancingMechanismPhysicalApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_physical_all_get**](BalancingMechanismPhysicalApi.md#balancing_physical_all_get) | **GET** /balancing/physical/all | Physical Datasets Market-wide
[**balancing_physical_get**](BalancingMechanismPhysicalApi.md#balancing_physical_get) | **GET** /balancing/physical | Physical Datasets Per-BMU


# **balancing_physical_all_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData balancing_physical_all_get(dataset, settlement_date, settlement_period=settlement_period, bm_unit=bm_unit, format=format)

Physical Datasets Market-wide

This endpoint provides the physical data for multiple requested BMUs or all BMUs.  It returns the data valid for a single settlement period.                Only one dataset can be queried at a time: PN, QPN, MILS, or MELS.  The results from each dataset are transformed to a common response model, with fields not present in all 4 datasets dropped.                The settlement period to query can be specified as a date and settlement period, or as a datetime  which will resolve to the settlement period that time falls within.    All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Note: When a settlementPeriod is supplied, the settlementDate parameter is treated as a Date only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.    Some examples of date parameter combinations are shown below.                Filtering by settlement date and period:                    /balancing/physical/all?dataset=PN&settlementDate=2023-01-18&settlementPeriod=3    Filtering by datetime:                    /balancing/physical/all?dataset=PN&settlementDate=2023-01-18T01:00Z

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_physical_physical_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData
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
    api_instance = openapi_client.BalancingMechanismPhysicalApi(api_client)
    dataset = 'dataset_example' # str | Dataset to query.
    settlement_date = '2023-01-18' # datetime | The settlement date or datetime for the filter.
    settlement_period = 3 # int | The settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    bm_unit = ['[\"2__HFLEX001\",\"HUMR-1\"]'] # List[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Physical Datasets Market-wide
        api_response = api_instance.balancing_physical_all_get(dataset, settlement_date, settlement_period=settlement_period, bm_unit=bm_unit, format=format)
        print("The response of BalancingMechanismPhysicalApi->balancing_physical_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingMechanismPhysicalApi->balancing_physical_all_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset to query. | 
 **settlement_date** | **datetime**| The settlement date or datetime for the filter. | 
 **settlement_period** | **int**| The settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **bm_unit** | [**List[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData.md)

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

# **balancing_physical_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData balancing_physical_get(bm_unit, var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, dataset=dataset, format=format)

Physical Datasets Per-BMU

This endpoint provides the physical data for a requested BMU.  It returns the data valid over a given time range.                By default, all of the relevant datasets are returned: PN, QPN, MILS, & MELS.  The results from each dataset are transformed to a common response model, with fields not present in all 4 datasets dropped.                By default, the from and to parameters filter the data by start time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of start time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_physical_physical_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData
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
    api_instance = openapi_client.BalancingMechanismPhysicalApi(api_client)
    bm_unit = '2__HFLEX001' # str | The BM Unit to query.
    var_from = '2022-09-22T00:00Z' # datetime | The \"from\" start time or settlement date for the filter.
    to = '2022-09-23T00:00Z' # datetime | The \"to\" start time or settlement date for the filter.
    settlement_period_from = 56 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    settlement_period_to = 56 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    dataset = ['[\"PN\",\"MILS\"]'] # List[str] | Datasets to filter. If empty, all datasets will be returned. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Physical Datasets Per-BMU
        api_response = api_instance.balancing_physical_get(bm_unit, var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, dataset=dataset, format=format)
        print("The response of BalancingMechanismPhysicalApi->balancing_physical_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingMechanismPhysicalApi->balancing_physical_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **var_from** | **datetime**| The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **dataset** | [**List[str]**](str.md)| Datasets to filter. If empty, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData.md)

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

