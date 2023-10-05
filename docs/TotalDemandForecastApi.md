# openapi_client.TotalDemandForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_demand_total_day_ahead_get**](TotalDemandForecastApi.md#forecast_demand_total_day_ahead_get) | **GET** /forecast/demand/total/day-ahead | Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620)
[**forecast_demand_total_week_ahead_get**](TotalDemandForecastApi.md#forecast_demand_total_week_ahead_get) | **GET** /forecast/demand/total/week-ahead | Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630) filtered by forecast week
[**forecast_demand_total_week_ahead_latest_get**](TotalDemandForecastApi.md#forecast_demand_total_week_ahead_latest_get) | **GET** /forecast/demand/total/week-ahead/latest | Latest Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630)


# **forecast_demand_total_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone forecast_demand_total_day_ahead_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620)

This endpoint provides day-ahead total load forecast per bidding zone data.  It can be filtered by settlement period dates.                This API endpoint has a maximum range of 7 days.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_day_ahead_total_load_per_bidding_zone import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone
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
    api_instance = openapi_client.TotalDemandForecastApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620)
        api_response = api_instance.forecast_demand_total_day_ahead_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TotalDemandForecastApi->forecast_demand_total_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TotalDemandForecastApi->forecast_demand_total_day_ahead_get: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone.md)

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

# **forecast_demand_total_week_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone forecast_demand_total_week_ahead_get(var_from, to, format=format)

Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630) filtered by forecast week

This endpoint returns week-ahead total load forecast per bidding zone data with the minimum possible  and maximum available total loads in MW values, filtered by forecast week.                For a given forecast date, if more than one forecast has been published, only the most recent forecast  is returned.                This API endpoint has a maximum range of 367 days.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_week_ahead_total_load_per_bidding_zone import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone
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
    api_instance = openapi_client.TotalDemandForecastApi(api_client)
    var_from = '2023-08-21' # date | The earliest forecast date to include.
    to = '2023-08-27' # date | The latest forecast date to include.
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630) filtered by forecast week
        api_response = api_instance.forecast_demand_total_week_ahead_get(var_from, to, format=format)
        print("The response of TotalDemandForecastApi->forecast_demand_total_week_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TotalDemandForecastApi->forecast_demand_total_week_ahead_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| The earliest forecast date to include. | 
 **to** | **date**| The latest forecast date to include. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone.md)

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

# **forecast_demand_total_week_ahead_latest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone forecast_demand_total_week_ahead_latest_get(format=format)

Latest Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630)

This endpoint returns the most recently published WATL / B0630 forecast.                This forecast is the week-ahead total load forecast per bidding zone data,  with minimum possible and maximum available total loads in MW values.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_week_ahead_total_load_per_bidding_zone import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone
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
    api_instance = openapi_client.TotalDemandForecastApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Latest Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630)
        api_response = api_instance.forecast_demand_total_week_ahead_latest_get(format=format)
        print("The response of TotalDemandForecastApi->forecast_demand_total_week_ahead_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TotalDemandForecastApi->forecast_demand_total_week_ahead_latest_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone.md)

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

