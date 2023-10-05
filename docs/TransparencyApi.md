# openapi_client.TransparencyApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demand_total_actual_get**](TransparencyApi.md#demand_total_actual_get) | **GET** /demand/total/actual | Actual Total Load Per Bidding Zone (ATL / B0610)
[**forecast_demand_total_day_ahead_get**](TransparencyApi.md#forecast_demand_total_day_ahead_get) | **GET** /forecast/demand/total/day-ahead | Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620)
[**forecast_demand_total_week_ahead_get**](TransparencyApi.md#forecast_demand_total_week_ahead_get) | **GET** /forecast/demand/total/week-ahead | Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630) filtered by forecast week
[**forecast_demand_total_week_ahead_latest_get**](TransparencyApi.md#forecast_demand_total_week_ahead_latest_get) | **GET** /forecast/demand/total/week-ahead/latest | Latest Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630)
[**forecast_generation_day_ahead_get**](TransparencyApi.md#forecast_generation_day_ahead_get) | **GET** /forecast/generation/day-ahead | Day-Ahead Aggregated Generation (DAG / B1430)
[**forecast_generation_wind_and_solar_day_ahead_get**](TransparencyApi.md#forecast_generation_wind_and_solar_day_ahead_get) | **GET** /forecast/generation/wind-and-solar/day-ahead | Day-Ahead Generation forecasts For Wind And Solar (DGWS / B1440)
[**generation_actual_per_type_day_total_get**](TransparencyApi.md#generation_actual_per_type_day_total_get) | **GET** /generation/actual/per-type/day-total | 24-hour Actual Generation Per Type (AGPT / B1620) summary data
[**generation_actual_per_type_get**](TransparencyApi.md#generation_actual_per_type_get) | **GET** /generation/actual/per-type | Actual Aggregated Generation Per Type (AGPT / B1620)
[**generation_actual_per_type_wind_and_solar_get**](TransparencyApi.md#generation_actual_per_type_wind_and_solar_get) | **GET** /generation/actual/per-type/wind-and-solar | Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630)


# **demand_total_actual_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone demand_total_actual_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Actual Total Load Per Bidding Zone (ATL / B0610)

This endpoint provides actual total load per bidding zone data.  It can be filtered by settlement period dates.                This API endpoint has a maximum range of 7 days.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_actual_total_load_per_bidding_zone import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone
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
    api_instance = openapi_client.TransparencyApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Actual Total Load Per Bidding Zone (ATL / B0610)
        api_response = api_instance.demand_total_actual_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TransparencyApi->demand_total_actual_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->demand_total_actual_get: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone.md)

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
    api_instance = openapi_client.TransparencyApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620)
        api_response = api_instance.forecast_demand_total_day_ahead_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TransparencyApi->forecast_demand_total_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->forecast_demand_total_day_ahead_get: %s\n" % e)
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
    api_instance = openapi_client.TransparencyApi(api_client)
    var_from = '2023-08-21' # date | The earliest forecast date to include.
    to = '2023-08-27' # date | The latest forecast date to include.
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630) filtered by forecast week
        api_response = api_instance.forecast_demand_total_week_ahead_get(var_from, to, format=format)
        print("The response of TransparencyApi->forecast_demand_total_week_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->forecast_demand_total_week_ahead_get: %s\n" % e)
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
    api_instance = openapi_client.TransparencyApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Latest Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630)
        api_response = api_instance.forecast_demand_total_week_ahead_latest_get(format=format)
        print("The response of TransparencyApi->forecast_demand_total_week_ahead_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->forecast_demand_total_week_ahead_latest_get: %s\n" % e)
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
    api_instance = openapi_client.TransparencyApi(api_client)
    var_from = '2023-07-20' # datetime | 
    to = '2023-07-22' # datetime | 
    settlement_period_from = 13 # int |  (optional)
    settlement_period_to = 19 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Day-Ahead Aggregated Generation (DAG / B1430)
        api_response = api_instance.forecast_generation_day_ahead_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TransparencyApi->forecast_generation_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->forecast_generation_day_ahead_get: %s\n" % e)
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
    api_instance = openapi_client.TransparencyApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    process_type = 'process_type_example' # str | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Day-Ahead Generation forecasts For Wind And Solar (DGWS / B1440)
        api_response = api_instance.forecast_generation_wind_and_solar_day_ahead_get(var_from, to, process_type, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TransparencyApi->forecast_generation_wind_and_solar_day_ahead_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->forecast_generation_wind_and_solar_day_ahead_get: %s\n" % e)
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

# **generation_actual_per_type_day_total_get**
> List[InsightsApiModelsResponsesTransparencyAgptSummaryData] generation_actual_per_type_day_total_get(format=format)

24-hour Actual Generation Per Type (AGPT / B1620) summary data

This endpoint provides aggregated AGPT (B1620) data. It returns totals and percentages  for the last half hour and 24 hours for each generation type.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_transparency_agpt_summary_data import InsightsApiModelsResponsesTransparencyAgptSummaryData
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
    api_instance = openapi_client.TransparencyApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # 24-hour Actual Generation Per Type (AGPT / B1620) summary data
        api_response = api_instance.generation_actual_per_type_day_total_get(format=format)
        print("The response of TransparencyApi->generation_actual_per_type_day_total_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->generation_actual_per_type_day_total_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**List[InsightsApiModelsResponsesTransparencyAgptSummaryData]**](InsightsApiModelsResponsesTransparencyAgptSummaryData.md)

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

# **generation_actual_per_type_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod generation_actual_per_type_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Actual Aggregated Generation Per Type (AGPT / B1620)

⚠ This endpoint provides a down-sampled data summary intended for visualisation purposes.  Depending on the quantity of data requested, data returned may be averaged hourly, daily,  weekly or monthly. Quantities are rounded to the nearest MWh.  Use /datasets/AGPT for full access.                This endpoint provides actual aggregated generation data per Power System Resource type   (Fuel Type categories as defined by Commission Regulation (EU) No 543/2013).    This endpoint filters by startTime, and groups results by settlement period.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_actual_generation_by_settlement_period import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod
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
    api_instance = openapi_client.TransparencyApi(api_client)
    var_from = '2023-07-20' # datetime | 
    to = '2023-07-22' # datetime | 
    settlement_period_from = 13 # int |  (optional)
    settlement_period_to = 19 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Actual Aggregated Generation Per Type (AGPT / B1620)
        api_response = api_instance.generation_actual_per_type_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TransparencyApi->generation_actual_per_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->generation_actual_per_type_get: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generation_actual_per_type_wind_and_solar_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar generation_actual_per_type_wind_and_solar_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630)

This endpoint provides actual or estimated wind and solar power generation  per settlement period. It returns generation with Power System Resource type  Solar, Wind Onshore or Wind Offshore (Fuel Type categories as defined by  Commission Regulation (EU) No 543/2013).                This endpoint filters by startTime and provides a maximum data output range of 7 days.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_actual_generation_wind_solar import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar
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
    api_instance = openapi_client.TransparencyApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630)
        api_response = api_instance.generation_actual_per_type_wind_and_solar_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of TransparencyApi->generation_actual_per_type_wind_and_solar_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransparencyApi->generation_actual_per_type_wind_and_solar_get: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar.md)

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

