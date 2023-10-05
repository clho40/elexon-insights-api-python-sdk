# openapi_client.WindGenerationForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_generation_wind_earliest_get**](WindGenerationForecastApi.md#forecast_generation_wind_earliest_get) | **GET** /forecast/generation/wind/earliest | Earliest wind generation forecast
[**forecast_generation_wind_earliest_stream_get**](WindGenerationForecastApi.md#forecast_generation_wind_earliest_stream_get) | **GET** /forecast/generation/wind/earliest/stream | Earliest wind generation forecast stream
[**forecast_generation_wind_evolution_get**](WindGenerationForecastApi.md#forecast_generation_wind_evolution_get) | **GET** /forecast/generation/wind/evolution | Evolution wind generation forecast
[**forecast_generation_wind_get**](WindGenerationForecastApi.md#forecast_generation_wind_get) | **GET** /forecast/generation/wind | Latest wind generation forecast
[**forecast_generation_wind_history_get**](WindGenerationForecastApi.md#forecast_generation_wind_history_get) | **GET** /forecast/generation/wind/history | Historical wind generation forecast
[**forecast_generation_wind_latest_get**](WindGenerationForecastApi.md#forecast_generation_wind_latest_get) | **GET** /forecast/generation/wind/latest | Latest wind generation forecast
[**forecast_generation_wind_latest_stream_get**](WindGenerationForecastApi.md#forecast_generation_wind_latest_stream_get) | **GET** /forecast/generation/wind/latest/stream | Latest wind generation forecast stream
[**forecast_generation_wind_peak_get**](WindGenerationForecastApi.md#forecast_generation_wind_peak_get) | **GET** /forecast/generation/wind/peak | Peak wind generation forecast


# **forecast_generation_wind_earliest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_earliest_get(var_from, to, format=format)

Earliest wind generation forecast

This endpoint provides the eariest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_wind_generation_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Earliest wind generation forecast
        api_response = api_instance.forecast_generation_wind_earliest_get(var_from, to, format=format)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_earliest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_earliest_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

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

# **forecast_generation_wind_earliest_stream_get**
> List[InsightsApiModelsServiceWindGenerationForecastRow] forecast_generation_wind_earliest_stream_get(var_from, to)

Earliest wind generation forecast stream

This endpoint provides the earliest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.  This endpoint has an optimised JSON payload and is aimed at frequent requests for the wind generation forecast data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_service_wind_generation_forecast_row import InsightsApiModelsServiceWindGenerationForecastRow
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Earliest wind generation forecast stream
        api_response = api_instance.forecast_generation_wind_earliest_stream_get(var_from, to)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_earliest_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_earliest_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**List[InsightsApiModelsServiceWindGenerationForecastRow]**](InsightsApiModelsServiceWindGenerationForecastRow.md)

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

# **forecast_generation_wind_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_evolution_get(start_time, format=format)

Evolution wind generation forecast

This endpoint provides the evolution wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_wind_generation_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution wind generation forecast
        api_response = api_instance.forecast_generation_wind_evolution_get(start_time, format=format)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

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

# **forecast_generation_wind_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_get(format=format)

Latest wind generation forecast

This endpoint provides the latest wind generation forecast data. This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30. Results are filtered by a range of DateTime parameters.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_wind_generation_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Latest wind generation forecast
        api_response = api_instance.forecast_generation_wind_get(format=format)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

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

# **forecast_generation_wind_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_history_get(publish_time, format=format)

Historical wind generation forecast

This endpoint provides the historical wind generation forecast data. This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_wind_generation_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historical wind generation forecast
        api_response = api_instance.forecast_generation_wind_history_get(publish_time, format=format)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

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

# **forecast_generation_wind_latest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_latest_get(var_from, to, format=format)

Latest wind generation forecast

This endpoint provides the latest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_wind_generation_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Latest wind generation forecast
        api_response = api_instance.forecast_generation_wind_latest_get(var_from, to, format=format)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_latest_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

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

# **forecast_generation_wind_latest_stream_get**
> List[InsightsApiModelsServiceWindGenerationForecastRow] forecast_generation_wind_latest_stream_get(var_from, to)

Latest wind generation forecast stream

This endpoint provides the latest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.  This endpoint has an optimised JSON payload and is aimed at frequent requests for the wind generation forecast data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_service_wind_generation_forecast_row import InsightsApiModelsServiceWindGenerationForecastRow
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Latest wind generation forecast stream
        api_response = api_instance.forecast_generation_wind_latest_stream_get(var_from, to)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_latest_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_latest_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**List[InsightsApiModelsServiceWindGenerationForecastRow]**](InsightsApiModelsServiceWindGenerationForecastRow.md)

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

# **forecast_generation_wind_peak_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_peak_get(var_from=var_from, to=to, format=format)

Peak wind generation forecast

This endpoint provides the peak wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_wind_generation_forecast import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast
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
    api_instance = openapi_client.WindGenerationForecastApi(api_client)
    var_from = '2021-10-01' # date | The start of the requested date range. (optional)
    to = '2021-10-30' # date | The end of the requested date range. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Peak wind generation forecast
        api_response = api_instance.forecast_generation_wind_peak_get(var_from=var_from, to=to, format=format)
        print("The response of WindGenerationForecastApi->forecast_generation_wind_peak_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WindGenerationForecastApi->forecast_generation_wind_peak_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

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

