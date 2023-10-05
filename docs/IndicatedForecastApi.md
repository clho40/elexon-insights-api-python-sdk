# openapi_client.IndicatedForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_indicated_day_ahead_evolution_get**](IndicatedForecastApi.md#forecast_indicated_day_ahead_evolution_get) | **GET** /forecast/indicated/day-ahead/evolution | Evolution Indicated day-ahead forecast
[**forecast_indicated_day_ahead_get**](IndicatedForecastApi.md#forecast_indicated_day_ahead_get) | **GET** /forecast/indicated/day-ahead | Latest indicated day-ahead forecast
[**forecast_indicated_day_ahead_history_get**](IndicatedForecastApi.md#forecast_indicated_day_ahead_history_get) | **GET** /forecast/indicated/day-ahead/history | Historical indicated day-ahead forecast


# **forecast_indicated_day_ahead_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast forecast_indicated_day_ahead_evolution_get(settlement_date, settlement_period, boundary=boundary, format=format)

Evolution Indicated day-ahead forecast

This endpoint provides the forecast indicated day-ahead data over time for the specified settlement date and settlement period.    Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_indicated_forecast_indicated_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast
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
    api_instance = openapi_client.IndicatedForecastApi(api_client)
    settlement_date = '2022-09-20' # date | The settlement date for the filter. This must be in the format yyyy-MM-dd.
    settlement_period = [1] # List[int] | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution Indicated day-ahead forecast
        api_response = api_instance.forecast_indicated_day_ahead_evolution_get(settlement_date, settlement_period, boundary=boundary, format=format)
        print("The response of IndicatedForecastApi->forecast_indicated_day_ahead_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatedForecastApi->forecast_indicated_day_ahead_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **settlement_period** | [**List[int]**](int.md)|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

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

# **forecast_indicated_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast forecast_indicated_day_ahead_get(boundary=boundary, format=format)

Latest indicated day-ahead forecast

This endpoint provides the latest forecast indicated day-ahead data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_indicated_forecast_indicated_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast
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
    api_instance = openapi_client.IndicatedForecastApi(api_client)
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Latest indicated day-ahead forecast
        api_response = api_instance.forecast_indicated_day_ahead_get(boundary=boundary, format=format)
        print("The response of IndicatedForecastApi->forecast_indicated_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatedForecastApi->forecast_indicated_day_ahead_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

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

# **forecast_indicated_day_ahead_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast forecast_indicated_day_ahead_history_get(publish_time, boundary=boundary, format=format)

Historical indicated day-ahead forecast



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_indicated_forecast_indicated_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast
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
    api_instance = openapi_client.IndicatedForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historical indicated day-ahead forecast
        api_response = api_instance.forecast_indicated_day_ahead_history_get(publish_time, boundary=boundary, format=format)
        print("The response of IndicatedForecastApi->forecast_indicated_day_ahead_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatedForecastApi->forecast_indicated_day_ahead_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

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

