# openapi_client.CreditDefaultNoticeApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_dn_get**](CreditDefaultNoticeApi.md#c_dn_get) | **GET** /CDN | Credit Default Notice (CDN)


# **c_dn_get**
> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse c_dn_get(format=format)

Credit Default Notice (CDN)

This endpoint provides a subset of CDN Index Data received from EC. It returns the defaults that are in force and defaults that have closed within the last 7 days.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_balancing_credit_default_notice_response import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse
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
    api_instance = openapi_client.CreditDefaultNoticeApi(api_client)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Credit Default Notice (CDN)
        api_response = api_instance.c_dn_get(format=format)
        print("The response of CreditDefaultNoticeApi->c_dn_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditDefaultNoticeApi->c_dn_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse**](InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse.md)

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

