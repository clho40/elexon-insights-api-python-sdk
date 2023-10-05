# openapi_client.MarginForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_margin_daily_evolution_get**](MarginForecastApi.md#forecast_margin_daily_evolution_get) | **GET** /forecast/margin/daily/evolution | Evolution Daily Margin Forecast
[**forecast_margin_daily_get**](MarginForecastApi.md#forecast_margin_daily_get) | **GET** /forecast/margin/daily | Daily Margin Forecast
[**forecast_margin_daily_history_get**](MarginForecastApi.md#forecast_margin_daily_history_get) | **GET** /forecast/margin/daily/history | Historical Daily Margin Forecast
[**forecast_margin_weekly_evolution_get**](MarginForecastApi.md#forecast_margin_weekly_evolution_get) | **GET** /forecast/margin/weekly/evolution | Evolution Daily Margin Forecast
[**forecast_margin_weekly_get**](MarginForecastApi.md#forecast_margin_weekly_get) | **GET** /forecast/margin/weekly | Weekly Margin Forecast
[**forecast_margin_weekly_history_get**](MarginForecastApi.md#forecast_margin_weekly_history_get) | **GET** /forecast/margin/weekly/history | Historical Weekly Margin Forecast


# **forecast_margin_daily_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily forecast_margin_daily_evolution_get(forecast_date, format=format)

Evolution Daily Margin Forecast

This endpoint provides the daily evolution Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily margin forecast for D+2 to D+14.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_forecast_margin_forecast_margin_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily
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
    api_instance = openapi_client.MarginForecastApi(api_client)
    forecast_date = '2022-09-20' # date | The forecast date for the filter. This must be in the format yyyy-MM-dd.
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution Daily Margin Forecast
        api_response = api_instance.forecast_margin_daily_evolution_get(forecast_date, format=format)
        print("The response of MarginForecastApi->forecast_margin_daily_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginForecastApi->forecast_margin_daily_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

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

# **forecast_margin_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily forecast_margin_daily_get(format=format)

Daily Margin Forecast

This endpoint provides the Generating Plant Operating Margin covering 2 days ahead to 14 days ahead  in MW values. The Daily API outputs the latest published data for daily margin forecast for D+2 t D+14

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_forecast_margin_forecast_margin_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily
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
    api_instance = openapi_client.MarginForecastApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Daily Margin Forecast
        api_response = api_instance.forecast_margin_daily_get(format=format)
        print("The response of MarginForecastApi->forecast_margin_daily_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginForecastApi->forecast_margin_daily_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

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

# **forecast_margin_daily_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily forecast_margin_daily_history_get(publish_time, format=format)

Historical Daily Margin Forecast

This endpoint provides the historic Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The historic API outputs the latest published data for historic daily margin forecast for D+2 to D+14

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_forecast_margin_forecast_margin_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily
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
    api_instance = openapi_client.MarginForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historical Daily Margin Forecast
        api_response = api_instance.forecast_margin_daily_history_get(publish_time, format=format)
        print("The response of MarginForecastApi->forecast_margin_daily_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginForecastApi->forecast_margin_daily_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

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

# **forecast_margin_weekly_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly forecast_margin_weekly_evolution_get(year, week, range=range, format=format)

Evolution Daily Margin Forecast

This endpoint provides the daily evolution Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily margin forecast for D+2 t D+14

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_forecast_margin_forecast_margin_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly
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
    api_instance = openapi_client.MarginForecastApi(api_client)
    year = 56 # int | 
    week = 56 # int | 
    range = 'range_example' # str |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution Daily Margin Forecast
        api_response = api_instance.forecast_margin_weekly_evolution_get(year, week, range=range, format=format)
        print("The response of MarginForecastApi->forecast_margin_weekly_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginForecastApi->forecast_margin_weekly_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **week** | **int**|  | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

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

# **forecast_margin_weekly_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly forecast_margin_weekly_get(range=range, format=format)

Weekly Margin Forecast

This endpoint provides the Generating Plant Operating Margin covering 2 weeks ahead to 156 weeks ahead in MW values.  The weekly API outputs the latest published data for weekly margin forecast for W+2 to W+156

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_forecast_margin_forecast_margin_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly
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
    api_instance = openapi_client.MarginForecastApi(api_client)
    range = 'range_example' # str |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Weekly Margin Forecast
        api_response = api_instance.forecast_margin_weekly_get(range=range, format=format)
        print("The response of MarginForecastApi->forecast_margin_weekly_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginForecastApi->forecast_margin_weekly_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

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

# **forecast_margin_weekly_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly forecast_margin_weekly_history_get(publish_time, range=range, format=format)

Historical Weekly Margin Forecast

This endpoint provides the weekly historic  Generating Plant Operating Margin.  This historic API output 2 weeks ahead to 156 weeks ahead in MW values

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_forecast_margin_forecast_margin_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly
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
    api_instance = openapi_client.MarginForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    range = 'range_example' # str |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historical Weekly Margin Forecast
        api_response = api_instance.forecast_margin_weekly_history_get(publish_time, range=range, format=format)
        print("The response of MarginForecastApi->forecast_margin_weekly_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginForecastApi->forecast_margin_weekly_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

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

