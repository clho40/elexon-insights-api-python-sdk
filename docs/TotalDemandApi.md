# openapi_client.TotalDemandApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demand_total_actual_get**](TotalDemandApi.md#demand_total_actual_get) | **GET** /demand/total/actual | Actual Total Load Per Bidding Zone (ATL / B0610)


# **demand_total_actual_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone demand_total_actual_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Actual Total Load Per Bidding Zone (ATL / B0610)

This endpoint provides actual total load per bidding zone data.  It can be filtered by settlement period dates.                This API endpoint has a maximum range of 7 days.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_actual_total_load_per_bidding_zone import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone
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
    api_instance = openapi_client.TotalDemandApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Actual Total Load Per Bidding Zone (ATL / B0610)
        api_response = api_instance.demand_total_actual_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TotalDemandApi->demand_total_actual_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TotalDemandApi->demand_total_actual_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **settlement_period_from** | **int**|  | [optional] 
 **settlement_period_to** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone.md)

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

