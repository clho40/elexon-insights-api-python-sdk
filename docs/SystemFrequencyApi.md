# openapi_client.SystemFrequencyApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_frequency_get**](SystemFrequencyApi.md#system_frequency_get) | **GET** /system/frequency | System Frequency
[**system_frequency_stream_get**](SystemFrequencyApi.md#system_frequency_stream_get) | **GET** /system/frequency/stream | System Frequency Stream


# **system_frequency_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency system_frequency_get(var_from=var_from, to=to, format=format)

System Frequency

This endpoint allows for retrieving a collection of recent system frequency data from National Grid ESO. Results  can be filtered by a range of DateTime parameters. This endpoint is useful for ad-hoc querying frequency data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_misc_system_frequency import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency
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
    api_instance = openapi_client.SystemFrequencyApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # System Frequency
        api_response = api_instance.system_frequency_get(var_from=var_from, to=to, format=format)
        print("The response of SystemFrequencyApi->system_frequency_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFrequencyApi->system_frequency_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency.md)

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

# **system_frequency_stream_get**
> List[InsightsApiModelsResponsesMiscSystemFrequency] system_frequency_stream_get(var_from=var_from, to=to)

System Frequency Stream

This endpoint allows for retrieving a stream of recent system frequency data from National Grid ESO. Results can  be filtered by a range of DateTime parameters. This endpoint has an optimised JSON payload and aimed at frequent  request for the frequency data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_misc_system_frequency import InsightsApiModelsResponsesMiscSystemFrequency
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
    api_instance = openapi_client.SystemFrequencyApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # System Frequency Stream
        api_response = api_instance.system_frequency_stream_get(var_from=var_from, to=to)
        print("The response of SystemFrequencyApi->system_frequency_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFrequencyApi->system_frequency_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 

### Return type

[**List[InsightsApiModelsResponsesMiscSystemFrequency]**](InsightsApiModelsResponsesMiscSystemFrequency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

