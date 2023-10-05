# openapi_client.AvailabilityApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generation_availability_summary14_d_get**](AvailabilityApi.md#generation_availability_summary14_d_get) | **GET** /generation/availability/summary/14D | Fourteen-day generation forecast
[**generation_availability_summary3_yw_get**](AvailabilityApi.md#generation_availability_summary3_yw_get) | **GET** /generation/availability/summary/3YW | Three-year generation forecast


# **generation_availability_summary14_d_get**
> List[InsightsApiModelsResponsesGenerationAggregatedForecast] generation_availability_summary14_d_get(format=format)

Fourteen-day generation forecast

This endpoint provides a summary of generation forecast data aggregated by forecast date,  intended for visualisation purposes. Use datasets endpoints for full dataset access.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_generation_aggregated_forecast import InsightsApiModelsResponsesGenerationAggregatedForecast
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
    api_instance = openapi_client.AvailabilityApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Fourteen-day generation forecast
        api_response = api_instance.generation_availability_summary14_d_get(format=format)
        print("The response of AvailabilityApi->generation_availability_summary14_d_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityApi->generation_availability_summary14_d_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**List[InsightsApiModelsResponsesGenerationAggregatedForecast]**](InsightsApiModelsResponsesGenerationAggregatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generation_availability_summary3_yw_get**
> List[InsightsApiModelsResponsesGenerationAggregatedForecast] generation_availability_summary3_yw_get(format=format)

Three-year generation forecast

This endpoint provides a summary of generation forecast data aggregated by forecast date,  intended for visualisation purposes. Use datasets endpoints for full dataset access.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_generation_aggregated_forecast import InsightsApiModelsResponsesGenerationAggregatedForecast
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
    api_instance = openapi_client.AvailabilityApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Three-year generation forecast
        api_response = api_instance.generation_availability_summary3_yw_get(format=format)
        print("The response of AvailabilityApi->generation_availability_summary3_yw_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityApi->generation_availability_summary3_yw_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**List[InsightsApiModelsResponsesGenerationAggregatedForecast]**](InsightsApiModelsResponsesGenerationAggregatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

