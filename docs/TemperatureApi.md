# openapi_client.TemperatureApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temperature_get**](TemperatureApi.md#temperature_get) | **GET** /temperature | Temperature Data


# **temperature_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData temperature_get(var_from=var_from, to=to, format=format)

Temperature Data

This endpoint provides daily average GB temperature data (in Celsius) as well as reference temperatures (low, normal and high).  This average data is calculated by National Grid ESO from the data retrieved from 6 weather stations around Britain.  NGESO use this data as part of the electricity demand forecasting process.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_misc_temperature_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData
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
    api_instance = openapi_client.TemperatureApi(api_client)
    var_from = '2022-09-20' # date | The from date for the filter. This must be in the format yyyy-MM-dd. (optional)
    to = '2022-09-21' # date | The to date for the filter. This must be in the format yyyy-MM-dd. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Temperature Data
        api_response = api_instance.temperature_get(var_from=var_from, to=to, format=format)
        print("The response of TemperatureApi->temperature_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemperatureApi->temperature_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| The from date for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **to** | **date**| The to date for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData.md)

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

