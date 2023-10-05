# openapi_client.AvailabilityForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_availability_daily_evolution_get**](AvailabilityForecastApi.md#forecast_availability_daily_evolution_get) | **GET** /forecast/availability/daily/evolution | Evolution Daily Generation Forecast
[**forecast_availability_daily_get**](AvailabilityForecastApi.md#forecast_availability_daily_get) | **GET** /forecast/availability/daily | Fourteen-day generation forecast
[**forecast_availability_daily_history_get**](AvailabilityForecastApi.md#forecast_availability_daily_history_get) | **GET** /forecast/availability/daily/history | Historic Fourteen-day generation forecast
[**forecast_availability_weekly_evolution_get**](AvailabilityForecastApi.md#forecast_availability_weekly_evolution_get) | **GET** /forecast/availability/weekly/evolution | Weekly Generation Forecast
[**forecast_availability_weekly_get**](AvailabilityForecastApi.md#forecast_availability_weekly_get) | **GET** /forecast/availability/weekly | Weekly Generation Forecast
[**forecast_availability_weekly_history_get**](AvailabilityForecastApi.md#forecast_availability_weekly_history_get) | **GET** /forecast/availability/weekly/history | Historic Weekly generation forecast


# **forecast_availability_daily_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily forecast_availability_daily_evolution_get(forecast_date, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Evolution Daily Generation Forecast

This endpoint provides the evolution of all daily generation forecasts over time for a given Forecast Date.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_availability_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily
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
    api_instance = openapi_client.AvailabilityForecastApi(api_client)
    forecast_date = '2022-09-20' # date | The forecast date for the filter. This must be in the format yyyy-MM-dd.
    level = 'level_example' # str |  (optional)
    bm_unit = ['bm_unit_example'] # List[str] |  (optional)
    fuel_type = ['fuel_type_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution Daily Generation Forecast
        api_response = api_instance.forecast_availability_daily_evolution_get(forecast_date, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
        print("The response of AvailabilityForecastApi->forecast_availability_daily_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityForecastApi->forecast_availability_daily_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

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

# **forecast_availability_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily forecast_availability_daily_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Fourteen-day generation forecast

This endpoint provides the latest fourteen-day generation forecast

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_availability_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily
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
    api_instance = openapi_client.AvailabilityForecastApi(api_client)
    level = 'level_example' # str |  (optional)
    bm_unit = ['bm_unit_example'] # List[str] |  (optional)
    fuel_type = ['fuel_type_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Fourteen-day generation forecast
        api_response = api_instance.forecast_availability_daily_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
        print("The response of AvailabilityForecastApi->forecast_availability_daily_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityForecastApi->forecast_availability_daily_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**|  | [optional] 
 **bm_unit** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

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

# **forecast_availability_daily_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily forecast_availability_daily_history_get(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Historic Fourteen-day generation forecast

This endpoint provides the latest fourteen-day generation forecast from a given DateTime

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_availability_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily
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
    api_instance = openapi_client.AvailabilityForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    level = 'level_example' # str |  (optional)
    bm_unit = ['bm_unit_example'] # List[str] |  (optional)
    fuel_type = ['fuel_type_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historic Fourteen-day generation forecast
        api_response = api_instance.forecast_availability_daily_history_get(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
        print("The response of AvailabilityForecastApi->forecast_availability_daily_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityForecastApi->forecast_availability_daily_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

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

# **forecast_availability_weekly_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly forecast_availability_weekly_evolution_get(year, week, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Weekly Generation Forecast

This endpoint provides all weekly generation forecasts over time for a given Year and Week

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_availability_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly
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
    api_instance = openapi_client.AvailabilityForecastApi(api_client)
    year = 56 # int | 
    week = 56 # int | 
    level = 'level_example' # str |  (optional)
    bm_unit = ['bm_unit_example'] # List[str] |  (optional)
    fuel_type = ['fuel_type_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Weekly Generation Forecast
        api_response = api_instance.forecast_availability_weekly_evolution_get(year, week, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
        print("The response of AvailabilityForecastApi->forecast_availability_weekly_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityForecastApi->forecast_availability_weekly_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **week** | **int**|  | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

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

# **forecast_availability_weekly_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly forecast_availability_weekly_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Weekly Generation Forecast

This endpoint provides the latest three-year generation forecast

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_availability_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly
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
    api_instance = openapi_client.AvailabilityForecastApi(api_client)
    level = 'level_example' # str |  (optional)
    bm_unit = ['bm_unit_example'] # List[str] |  (optional)
    fuel_type = ['fuel_type_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Weekly Generation Forecast
        api_response = api_instance.forecast_availability_weekly_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
        print("The response of AvailabilityForecastApi->forecast_availability_weekly_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityForecastApi->forecast_availability_weekly_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**|  | [optional] 
 **bm_unit** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

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

# **forecast_availability_weekly_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly forecast_availability_weekly_history_get(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Historic Weekly generation forecast

This endpoint provides the latest three-year forecast from a given DateTime

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_availability_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly
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
    api_instance = openapi_client.AvailabilityForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    level = 'level_example' # str |  (optional)
    bm_unit = ['bm_unit_example'] # List[str] |  (optional)
    fuel_type = ['fuel_type_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historic Weekly generation forecast
        api_response = api_instance.forecast_availability_weekly_history_get(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
        print("The response of AvailabilityForecastApi->forecast_availability_weekly_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityForecastApi->forecast_availability_weekly_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

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

