# openapi_client.ActualGenerationApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generation_actual_per_type_day_total_get**](ActualGenerationApi.md#generation_actual_per_type_day_total_get) | **GET** /generation/actual/per-type/day-total | 24-hour Actual Generation Per Type (AGPT / B1620) summary data
[**generation_actual_per_type_get**](ActualGenerationApi.md#generation_actual_per_type_get) | **GET** /generation/actual/per-type | Actual Aggregated Generation Per Type (AGPT / B1620)
[**generation_actual_per_type_wind_and_solar_get**](ActualGenerationApi.md#generation_actual_per_type_wind_and_solar_get) | **GET** /generation/actual/per-type/wind-and-solar | Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630)


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
    api_instance = openapi_client.ActualGenerationApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # 24-hour Actual Generation Per Type (AGPT / B1620) summary data
        api_response = api_instance.generation_actual_per_type_day_total_get(format=format)
        print("The response of ActualGenerationApi->generation_actual_per_type_day_total_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActualGenerationApi->generation_actual_per_type_day_total_get: %s\n" % e)
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
    api_instance = openapi_client.ActualGenerationApi(api_client)
    var_from = '2023-07-20' # datetime | 
    to = '2023-07-22' # datetime | 
    settlement_period_from = 13 # int |  (optional)
    settlement_period_to = 19 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Actual Aggregated Generation Per Type (AGPT / B1620)
        api_response = api_instance.generation_actual_per_type_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of ActualGenerationApi->generation_actual_per_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActualGenerationApi->generation_actual_per_type_get: %s\n" % e)
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
    api_instance = openapi_client.ActualGenerationApi(api_client)
    var_from = '2023-07-18' # datetime | 
    to = '2023-07-21' # datetime | 
    settlement_period_from = 36 # int |  (optional)
    settlement_period_to = 12 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630)
        api_response = api_instance.generation_actual_per_type_wind_and_solar_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of ActualGenerationApi->generation_actual_per_type_wind_and_solar_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActualGenerationApi->generation_actual_per_type_wind_and_solar_get: %s\n" % e)
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

