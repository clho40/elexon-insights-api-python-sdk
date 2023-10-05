# openapi_client.SystemWarningsApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_warnings_get**](SystemWarningsApi.md#system_warnings_get) | **GET** /system/warnings | System Warnings


# **system_warnings_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData system_warnings_get(warning_type=warning_type, publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, format=format)

System Warnings

This endpoint provides system warnings data. Results can be filtered by warning type and a range of DateTime parameters.  - If no parameters are specified then the latest message is returned  - If just a warning type is specified then the latest message of that type is returned  - If just publish times are specified then all messages within that range are returned

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_misc_system_warnings_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData
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
    api_instance = openapi_client.SystemWarningsApi(api_client)
    warning_type = 'IT SYSTEMS OUTAGE' # str |  (optional)
    publish_date_time_from = '2023/06/01 07:00' # datetime |  (optional)
    publish_date_time_to = '2023/06/30 10:00' # datetime |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # System Warnings
        api_response = api_instance.system_warnings_get(warning_type=warning_type, publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, format=format)
        print("The response of SystemWarningsApi->system_warnings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemWarningsApi->system_warnings_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warning_type** | **str**|  | [optional] 
 **publish_date_time_from** | **datetime**|  | [optional] 
 **publish_date_time_to** | **datetime**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData.md)

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

