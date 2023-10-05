# openapi_client.GenerationOutturnApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generation_outturn_fuelinsthhcur_get**](GenerationOutturnApi.md#generation_outturn_fuelinsthhcur_get) | **GET** /generation/outturn/FUELINSTHHCUR | Generation by fuel type categories (FUELINSTHHCUR)
[**generation_outturn_half_hourly_interconnector_get**](GenerationOutturnApi.md#generation_outturn_half_hourly_interconnector_get) | **GET** /generation/outturn/halfHourlyInterconnector | Interconnector Flow
[**generation_outturn_summary_get**](GenerationOutturnApi.md#generation_outturn_summary_get) | **GET** /generation/outturn/summary | Outturn Summary


# **generation_outturn_fuelinsthhcur_get**
> List[InsightsApiModelsResponsesGenerationGenerationByFuelType] generation_outturn_fuelinsthhcur_get(fuel_type=fuel_type, format=format)

Generation by fuel type categories (FUELINSTHHCUR)

This endpoint provides a snapshot view of the last 24 hours generation by individual fuel type categories including interconnector.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_generation_generation_by_fuel_type import InsightsApiModelsResponsesGenerationGenerationByFuelType
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
    api_instance = openapi_client.GenerationOutturnApi(api_client)
    fuel_type = ['fuel_type_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Generation by fuel type categories (FUELINSTHHCUR)
        api_response = api_instance.generation_outturn_fuelinsthhcur_get(fuel_type=fuel_type, format=format)
        print("The response of GenerationOutturnApi->generation_outturn_fuelinsthhcur_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationOutturnApi->generation_outturn_fuelinsthhcur_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**List[InsightsApiModelsResponsesGenerationGenerationByFuelType]**](InsightsApiModelsResponsesGenerationGenerationByFuelType.md)

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

# **generation_outturn_half_hourly_interconnector_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn generation_outturn_half_hourly_interconnector_get(publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, interconnector_name=interconnector_name, format=format)

Interconnector Flow

This endpoint provides the interconnector flows report derived from the Generation by Fuel Type (FUELINST)  data and shows both interconnector imports and exports; the data is updated every five minutes.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_half_hourly_interconnector_outturn import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn
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
    api_instance = openapi_client.GenerationOutturnApi(api_client)
    publish_date_time_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    publish_date_time_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    settlement_date_from = '2022-09-20' # date | The settlement date from filter. This must be in the format yyyy-MM-dd. (optional)
    settlement_date_to = '2022-09-21' # date | The settlement date to filter. This must be in the format yyyy-MM-dd. (optional)
    settlement_period = [56] # List[int] |  (optional)
    interconnector_name = ['interconnector_name_example'] # List[str] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Interconnector Flow
        api_response = api_instance.generation_outturn_half_hourly_interconnector_get(publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, interconnector_name=interconnector_name, format=format)
        print("The response of GenerationOutturnApi->generation_outturn_half_hourly_interconnector_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationOutturnApi->generation_outturn_half_hourly_interconnector_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_date_time_from** | **datetime**|  | [optional] 
 **publish_date_time_to** | **datetime**|  | [optional] 
 **settlement_date_from** | **date**| The settlement date from filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| The settlement date to filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**List[int]**](int.md)|  | [optional] 
 **interconnector_name** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn.md)

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

# **generation_outturn_summary_get**
> List[InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod] generation_outturn_summary_get(start_time=start_time, end_time=end_time, include_negative_generation=include_negative_generation, format=format)

Outturn Summary

⚠ This endpoint provides a down-sampled data summary intended for visualisation purposes.  Use raw dataset endpoints under /datasets for full access.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_generation_outturn_generation_by_settlement_period import InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod
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
    api_instance = openapi_client.GenerationOutturnApi(api_client)
    start_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    include_negative_generation = True # bool |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Outturn Summary
        api_response = api_instance.generation_outturn_summary_get(start_time=start_time, end_time=end_time, include_negative_generation=include_negative_generation, format=format)
        print("The response of GenerationOutturnApi->generation_outturn_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationOutturnApi->generation_outturn_summary_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**|  | [optional] 
 **end_time** | **datetime**|  | [optional] 
 **include_negative_generation** | **bool**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**List[InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod]**](InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod.md)

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

