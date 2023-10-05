# openapi_client.NonBMVolumesApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_nonbm_volumes_get**](NonBMVolumesApi.md#balancing_nonbm_volumes_get) | **GET** /balancing/nonbm/volumes | Balancing Services Volume


# **balancing_nonbm_volumes_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume balancing_nonbm_volumes_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, bm_unit=bm_unit, format=format)

Balancing Services Volume

This endpoint provides Balancing Services Volume data received from NGESO, with an added computed 'Time' field.  (The time field is calculated from the settlement date & period and represents the earliest possible time for  for which the datapoint applies)                Balancing Services Volume is a volume which is received from the System Operator, which represents the volume  of energy (MWh) associated with the provision of Applicable Balancing Services for each relevant BM Unit and  Settlement Period.    QAS can be positive or negative and is normally only provided where there is a non-zero volume.                By default, the from and to parameters filter the data by time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_balancing_services_volume import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume
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
    api_instance = openapi_client.NonBMVolumesApi(api_client)
    var_from = '2022-08-12T00:00Z' # datetime | The \"from\" start time or settlement date for the filter.
    to = '2022-08-13T00:00Z' # datetime | The \"to\" start time or settlement date for the filter.
    settlement_period_from = 56 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    settlement_period_to = 56 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
    bm_unit = ['[\"T_CNQPS-1\"]'] # List[str] | The BM units to query. Add each unit separately. If no BM unit is selected all BM units will be displayed. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Balancing Services Volume
        api_response = api_instance.balancing_nonbm_volumes_get(var_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, bm_unit=bm_unit, format=format)
        print("The response of NonBMVolumesApi->balancing_nonbm_volumes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonBMVolumesApi->balancing_nonbm_volumes_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **bm_unit** | [**List[str]**](str.md)| The BM units to query. Add each unit separately. If no BM unit is selected all BM units will be displayed. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume.md)

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

