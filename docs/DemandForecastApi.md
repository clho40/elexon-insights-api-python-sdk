# openapi_client.DemandForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_demand_daily_evolution_get**](DemandForecastApi.md#forecast_demand_daily_evolution_get) | **GET** /forecast/demand/daily/evolution | Evolution Daily Demand Forecast
[**forecast_demand_daily_get**](DemandForecastApi.md#forecast_demand_daily_get) | **GET** /forecast/demand/daily | Fourteen day forecast demand
[**forecast_demand_daily_history_get**](DemandForecastApi.md#forecast_demand_daily_history_get) | **GET** /forecast/demand/daily/history | Historical daily forecast demand
[**forecast_demand_day_ahead_earliest_get**](DemandForecastApi.md#forecast_demand_day_ahead_earliest_get) | **GET** /forecast/demand/day-ahead/earliest | Earliest published day-ahead demand forecast data for a given settlement period
[**forecast_demand_day_ahead_earliest_stream_get**](DemandForecastApi.md#forecast_demand_day_ahead_earliest_stream_get) | **GET** /forecast/demand/day-ahead/earliest/stream | Stream of earliest day-ahead demand forecast data for a given settlement period
[**forecast_demand_day_ahead_evolution_get**](DemandForecastApi.md#forecast_demand_day_ahead_evolution_get) | **GET** /forecast/demand/day-ahead/evolution | Evolution Day-ahead Demand forecast
[**forecast_demand_day_ahead_get**](DemandForecastApi.md#forecast_demand_day_ahead_get) | **GET** /forecast/demand/day-ahead | Day-ahead demand forecast
[**forecast_demand_day_ahead_history_get**](DemandForecastApi.md#forecast_demand_day_ahead_history_get) | **GET** /forecast/demand/day-ahead/history | Historical day-ahead forecast demand
[**forecast_demand_day_ahead_latest_get**](DemandForecastApi.md#forecast_demand_day_ahead_latest_get) | **GET** /forecast/demand/day-ahead/latest | Latest published day-ahead demand forecast data for a given settlement period
[**forecast_demand_day_ahead_latest_stream_get**](DemandForecastApi.md#forecast_demand_day_ahead_latest_stream_get) | **GET** /forecast/demand/day-ahead/latest/stream | Stream of latest published day-ahead demand forecast data for a given settlement period
[**forecast_demand_day_ahead_peak_get**](DemandForecastApi.md#forecast_demand_day_ahead_peak_get) | **GET** /forecast/demand/day-ahead/peak | Retrieve peak demand data for each day, based on Day Ahead forecast data
[**forecast_demand_weekly_evolution_get**](DemandForecastApi.md#forecast_demand_weekly_evolution_get) | **GET** /forecast/demand/weekly/evolution | Evolution Weekly Demand Forecast
[**forecast_demand_weekly_get**](DemandForecastApi.md#forecast_demand_weekly_get) | **GET** /forecast/demand/weekly | Weekly forecast demand
[**forecast_demand_weekly_history_get**](DemandForecastApi.md#forecast_demand_weekly_history_get) | **GET** /forecast/demand/weekly/history | Historical weekly forecast demand


# **forecast_demand_daily_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily forecast_demand_daily_evolution_get(forecast_date, format=format)

Evolution Daily Demand Forecast

This endpoint provides the evolution of all daily demand forecasts over time for a given forecast date.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    forecast_date = '2022-09-20' # date | The forecast date for the filter. This must be in the format yyyy-MM-dd.
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution Daily Demand Forecast
        api_response = api_instance.forecast_demand_daily_evolution_get(forecast_date, format=format)
        print("The response of DemandForecastApi->forecast_demand_daily_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_daily_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)

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

# **forecast_demand_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily forecast_demand_daily_get(format=format)

Fourteen day forecast demand

Retrieve latest 14-day forecast demand data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Fourteen day forecast demand
        api_response = api_instance.forecast_demand_daily_get(format=format)
        print("The response of DemandForecastApi->forecast_demand_daily_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_daily_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_daily_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily forecast_demand_daily_history_get(publish_time, format=format)

Historical daily forecast demand

Retrieve historical daily forecast demand data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_daily import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historical daily forecast demand
        api_response = api_instance.forecast_demand_daily_history_get(publish_time, format=format)
        print("The response of DemandForecastApi->forecast_demand_daily_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_daily_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)

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

# **forecast_demand_day_ahead_earliest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_earliest_get(var_from, to, boundary=boundary, format=format)

Earliest published day-ahead demand forecast data for a given settlement period

This endpoint allows for retrieving earliest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the earliest published forecast for each settlement period is shown.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_day_ahead import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Earliest published day-ahead demand forecast data for a given settlement period
        api_response = api_instance.forecast_demand_day_ahead_earliest_get(var_from, to, boundary=boundary, format=format)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_earliest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_earliest_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

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

# **forecast_demand_day_ahead_earliest_stream_get**
> List[InsightsApiModelsServiceDayAheadDemandForecastRow] forecast_demand_day_ahead_earliest_stream_get(var_from, to, boundary=boundary)

Stream of earliest day-ahead demand forecast data for a given settlement period

This endpoint allows for retrieving a stream of earliest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the earliest published forecast for each settlement period is shown.  This endpoint has an optimised JSON payload and aimed at frequent request for the day-ahead demand forecast data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_service_day_ahead_demand_forecast_row import InsightsApiModelsServiceDayAheadDemandForecastRow
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)

    try:
        # Stream of earliest day-ahead demand forecast data for a given settlement period
        api_response = api_instance.forecast_demand_day_ahead_earliest_stream_get(var_from, to, boundary=boundary)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_earliest_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_earliest_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 

### Return type

[**List[InsightsApiModelsServiceDayAheadDemandForecastRow]**](InsightsApiModelsServiceDayAheadDemandForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_evolution_get(settlement_date, settlement_period, boundary=boundary, format=format)

Evolution Day-ahead Demand forecast

This endpoint provides the day and day ahead demand forecast and are categorized as National Demand Forecast (NDF) and Transmission System Demand Forecast (TSDF);  the forecast values are derived by NGESO and is based on historically metered generation output for Great Britain.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period.  NDF takes into account transmission losses but but does not include station transformer load, pumped storage demand or Interconnector demand;  the data is reported only at national level; and TSDF which takes into account transmission losses , station transformer load, pumped storage demand and interconnector demand.  The data is reported both at national and boundary (system zones) level. Boundary data only available for Transmission System Demand Forecast (TSDF).                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_day_ahead import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    settlement_date = '2022-09-20' # date | The settlement date for the filter. This must be in the format yyyy-MM-dd.
    settlement_period = [1] # List[int] | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution Day-ahead Demand forecast
        api_response = api_instance.forecast_demand_day_ahead_evolution_get(settlement_date, settlement_period, boundary=boundary, format=format)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **settlement_period** | [**List[int]**](int.md)|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

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

# **forecast_demand_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_get(boundary=boundary, format=format)

Day-ahead demand forecast

This endpoint provides the day and day ahead demand forecast and are categorized as National Demand Forecast (NDF) and Transmission System Demand Forecast (TSDF);  the forecast values are derived by NGESO and is based on historically metered generation output for Great Britain.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period.  NDF takes into account transmission losses but but does not include station transformer load, pumped storage demand or Interconnector demand;  the data is reported only at national level; and TSDF which takes into account transmission losses , station transformer load, pumped storage demand and interconnector demand.  The data is reported both at national and boundary (system zones) level. Boundary data only available for Transmission System Demand Forecast (TSDF).

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_day_ahead import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Day-ahead demand forecast
        api_response = api_instance.forecast_demand_day_ahead_get(boundary=boundary, format=format)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

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

# **forecast_demand_day_ahead_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_history_get(publish_time, boundary=boundary, format=format)

Historical day-ahead forecast demand

This endpoint provides the day and day ahead demand forecast and are categorized as National Demand Forecast (NDF) and Transmission System Demand Forecast (TSDF);  the forecast values are derived by NGESO and is based on historically metered generation output for Great Britain.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period.  NDF takes into account transmission losses but but does not include station transformer load, pumped storage demand or Interconnector demand;  the data is reported only at national level; and TSDF which takes into account transmission losses , station transformer load, pumped storage demand and interconnector demand.  The data is reported both at national and boundary (system zones) level. Boundary data only available for Transmission System Demand Forecast (TSDF).

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_day_ahead import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historical day-ahead forecast demand
        api_response = api_instance.forecast_demand_day_ahead_history_get(publish_time, boundary=boundary, format=format)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

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

# **forecast_demand_day_ahead_latest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_latest_get(var_from, to, boundary=boundary, format=format)

Latest published day-ahead demand forecast data for a given settlement period

This endpoint allows for retrieving latest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the latest published forecast for each settlement period is shown.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_day_ahead import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Latest published day-ahead demand forecast data for a given settlement period
        api_response = api_instance.forecast_demand_day_ahead_latest_get(var_from, to, boundary=boundary, format=format)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_latest_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

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

# **forecast_demand_day_ahead_latest_stream_get**
> List[InsightsApiModelsServiceDayAheadDemandForecastRow] forecast_demand_day_ahead_latest_stream_get(var_from, to, boundary=boundary)

Stream of latest published day-ahead demand forecast data for a given settlement period

This endpoint allows for retrieving a stream of latest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the latest published forecast for each settlement period is shown.  This endpoint has an optimised JSON payload and aimed at frequent request for the day-ahead demand forecast data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_service_day_ahead_demand_forecast_row import InsightsApiModelsServiceDayAheadDemandForecastRow
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | 
    to = '2013-10-20T19:20:30+01:00' # datetime | 
    boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)

    try:
        # Stream of latest published day-ahead demand forecast data for a given settlement period
        api_response = api_instance.forecast_demand_day_ahead_latest_stream_get(var_from, to, boundary=boundary)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_latest_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_latest_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 

### Return type

[**List[InsightsApiModelsServiceDayAheadDemandForecastRow]**](InsightsApiModelsServiceDayAheadDemandForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_peak_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak forecast_demand_day_ahead_peak_get(boundary=boundary, var_from=var_from, to=to, format=format)

Retrieve peak demand data for each day, based on Day Ahead forecast data

This endpoint allows for retrieving the peak demand that is forecast for each day from National Grid ESO.  Results are filtered by a range of Date parameters.  Results default to yesterday, today and tomorrow if no parameters are supplied.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_peak import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    boundary = 'boundary_example' # str |  (optional)
    var_from = '2021-10-01' # date | The start of the requested date range. (optional)
    to = '2021-10-30' # date | The end of the requested date range. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Retrieve peak demand data for each day, based on Day Ahead forecast data
        api_response = api_instance.forecast_demand_day_ahead_peak_get(boundary=boundary, var_from=var_from, to=to, format=format)
        print("The response of DemandForecastApi->forecast_demand_day_ahead_peak_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_peak_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary** | **str**|  | [optional] 
 **var_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak.md)

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

# **forecast_demand_weekly_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly forecast_demand_weekly_evolution_get(forecast_year, forecast_week, format=format)

Evolution Weekly Demand Forecast

This endpoint provides all weekly demand forecasts over time for a given forecast Year and Week

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    forecast_year = 56 # int | 
    forecast_week = 56 # int | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Evolution Weekly Demand Forecast
        api_response = api_instance.forecast_demand_weekly_evolution_get(forecast_year, forecast_week, format=format)
        print("The response of DemandForecastApi->forecast_demand_weekly_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_weekly_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_year** | **int**|  | 
 **forecast_week** | **int**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)

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

# **forecast_demand_weekly_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly forecast_demand_weekly_get(format=format)

Weekly forecast demand

This endpoint provides the latest weekly forecast demand data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Weekly forecast demand
        api_response = api_instance.forecast_demand_weekly_get(format=format)
        print("The response of DemandForecastApi->forecast_demand_weekly_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_weekly_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_weekly_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly forecast_demand_weekly_history_get(publish_time, format=format)

Historical weekly forecast demand

Retrieve historical weekly forecast demand data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_forecast_demand_forecast_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly
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
    api_instance = openapi_client.DemandForecastApi(api_client)
    publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Historical weekly forecast demand
        api_response = api_instance.forecast_demand_weekly_history_get(publish_time, format=format)
        print("The response of DemandForecastApi->forecast_demand_weekly_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandForecastApi->forecast_demand_weekly_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)

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

