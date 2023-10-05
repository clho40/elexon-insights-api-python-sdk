# openapi_client.LossOfLoadProbabilityAndDeratedMarginApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lolpdrm_forecast_evolution_get**](LossOfLoadProbabilityAndDeratedMarginApi.md#lolpdrm_forecast_evolution_get) | **GET** /lolpdrm/forecast/evolution | Loss of Load Probability and De-rated Margin forecasts per settlement period


# **lolpdrm_forecast_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse lolpdrm_forecast_evolution_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Loss of Load Probability and De-rated Margin forecasts per settlement period

This endpoint provides the 1h, 2h, 4h, 8h and 12h+ Loss of Load Probability and De-rated Margin forecasts  for each settlement period over a requested time range.                For each forecast horizon at 1, 2, 4 or 8 hours, the returned value is the forecast received that number of hours  before the start of the settlement period.                For the forecast horizon of 12h, the returned value is the most recent forecast received 12 or more hours  before the start of the settlement period. That is, if the most recent forecast was published today at 00:00,  - for 11:30 today, the 12h forecast is the one published yesterday at 23:30 (12h before)  - for 12:00 today, the 12h forecast is the one published today at 00:00 (12h before)  - for 12:30 today, the 12h forecast is the one published today at 00:00 (the latest published)

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse
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
    api_instance = openapi_client.LossOfLoadProbabilityAndDeratedMarginApi(api_client)
    var_from = '2023-03-06T07:00Z' # datetime | 
    to = '2023-03-06T12:00Z' # datetime | 
    settlement_period_from = 15 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    settlement_period_to = 25 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Loss of Load Probability and De-rated Margin forecasts per settlement period
        api_response = api_instance.lolpdrm_forecast_evolution_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
        print("The response of LossOfLoadProbabilityAndDeratedMarginApi->lolpdrm_forecast_evolution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LossOfLoadProbabilityAndDeratedMarginApi->lolpdrm_forecast_evolution_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse.md)

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

