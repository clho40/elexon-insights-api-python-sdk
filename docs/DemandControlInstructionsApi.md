# openapi_client.DemandControlInstructionsApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_demand_control_instructions_get**](DemandControlInstructionsApi.md#system_demand_control_instructions_get) | **GET** /system/demand-control-instructions | Demand Control Instruction (DCI)


# **system_demand_control_instructions_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData system_demand_control_instructions_get(var_from=var_from, to=to, format=format)

Demand Control Instruction (DCI)

This endpoint provides demand control instruction data, filtered by the time range of the instruction.  There is no date range limit on parameters.  If no query parameters are supplied all data is returned.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_misc_demand_control_instruction_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData
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
    api_instance = openapi_client.DemandControlInstructionsApi(api_client)
    var_from = '2021-04-30T00:00Z' # datetime |  (optional)
    to = '2021-04-30T20:00Z' # datetime |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Demand Control Instruction (DCI)
        api_response = api_instance.system_demand_control_instructions_get(var_from=var_from, to=to, format=format)
        print("The response of DemandControlInstructionsApi->system_demand_control_instructions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandControlInstructionsApi->system_demand_control_instructions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData.md)

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

