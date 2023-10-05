# openapi_client.GenerationForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_generation_day_ahead_get**](GenerationForecastApi.md#forecast_generation_day_ahead_get) | **GET** /forecast/generation/day-ahead | Day-Ahead Aggregated Generation (DAG / B1430)
[**forecast_generation_wind_and_solar_day_ahead_get**](GenerationForecastApi.md#forecast_generation_wind_and_solar_day_ahead_get) | **GET** /forecast/generation/wind-and-solar/day-ahead | Day-Ahead Generation forecasts For Wind And Solar (DGWS / B1440)


# **forecast_generation_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration forecast_generation_day_ahead_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-Ahead Aggregated Generation (DAG / B1430)

This endpoint provides day-ahead aggregated generation data filtered by settlement date.                This API endpoint has a maximum range of 7 days.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_day_ahead_aggregated_generation import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration
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
    api_instance = openapi_client.GenerationForecastApi(api_client)
    var_from = '2023-07-20' # datetime | 
    to = '2023-07-22' # datetime | 
    settlement_period_from = 13 # int |  (optional)
    settlement_period_to = 19 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Day-Ahead Aggregated Generation (DAG / B1430)
        api_response = api_instance.forecast_generation_day_ahead_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of GenerationForecastApi->forecast_generation_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationForecastApi->forecast_generation_day_ahead_get: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration.md)

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

# **forecast_generation_wind_and_solar_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar forecast_generation_wind_and_solar_day_ahead_get(var_from, to, process_type, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-Ahead Generation forecasts For Wind And Solar (DGWS / B1440)

This endpoint provides day-ahead forecast generation data for wind and solar.                This endpoint filters by startTime and provides a maximum data output range of 7 days.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar
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
    api_instance = openapi_client.GenerationForecastApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    process_type = 'process_type_example' # str | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Day-Ahead Generation forecasts For Wind And Solar (DGWS / B1440)
        api_response = api_instance.forecast_generation_wind_and_solar_day_ahead_get(var_from, to, process_type, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of GenerationForecastApi->forecast_generation_wind_and_solar_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationForecastApi->forecast_generation_wind_and_solar_day_ahead_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **process_type** | **str**|  | 
 **settlement_period_from** | **int**|  | [optional] 
 **settlement_period_to** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar.md)

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

