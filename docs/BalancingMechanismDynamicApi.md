# openapi_client.BalancingMechanismDynamicApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_dynamic_all_get**](BalancingMechanismDynamicApi.md#balancing_dynamic_all_get) | **GET** /balancing/dynamic/all | Dynamic Datasets Market-wide
[**balancing_dynamic_get**](BalancingMechanismDynamicApi.md#balancing_dynamic_get) | **GET** /balancing/dynamic | Dynamic Datasets Per-BMU
[**balancing_dynamic_rates_all_get**](BalancingMechanismDynamicApi.md#balancing_dynamic_rates_all_get) | **GET** /balancing/dynamic/rates/all | Rate Datasets Market-Wide
[**balancing_dynamic_rates_get**](BalancingMechanismDynamicApi.md#balancing_dynamic_rates_get) | **GET** /balancing/dynamic/rates | Rate Datasets Per-BMU


# **balancing_dynamic_all_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData balancing_dynamic_all_get(settlement_date, settlement_period=settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)

Dynamic Datasets Market-wide

This endpoint provides the dynamic data for multiple requested BMUs or all BMUs, excluding dynamic rate data.  It returns the data valid for a single settlement period. This includes a snapshot of data valid at the start  of the settlement period, and any changes published during that settlement period.                By default, all of the relevant datasets are returned: SIL, SEL, NDZ, NTB, NTO, MZT, MNZT, MDV & MDP.  The results from each dataset are transformed to a common response model, with the common integer field *Value*  mapped from the fields *Level*, *Period*, *Volume* or *Notice* in the original dataset, as relevant.                The settlement period to query can be specified as a date and settlement period, or as a datetime  which will resolve to the settlement period that time falls within.    All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.    Some examples of date parameter combinations are shown below.                Filtering by datetime:                    /balancing/dynamic/all?settlementDate=2023-01-18T01:00Z                Filtering by settlement date and period:                    /balancing/dynamic/all?settlementDate=2023-01-18&settlementPeriod=3

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_dynamic_dynamic_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData
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
    api_instance = openapi_client.BalancingMechanismDynamicApi(api_client)
    settlement_date = '2023-01-18' # datetime | The settlement date or datetime to filter.
    settlement_period = 3 # int | The settlement period to filter. This should be an integer from 1-50 inclusive. (optional)
    bm_unit = ['[\"2__HFLEX001\",\"HUMR-1\"]'] # List[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
    dataset = ['[\"SEL\",\"MNZT\",\"MDP\"]'] # List[str] | Datasets to filter. If omitted, all datasets will be returned. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Dynamic Datasets Market-wide
        api_response = api_instance.balancing_dynamic_all_get(settlement_date, settlement_period=settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)
        print("The response of BalancingMechanismDynamicApi->balancing_dynamic_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingMechanismDynamicApi->balancing_dynamic_all_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **datetime**| The settlement date or datetime to filter. | 
 **settlement_period** | **int**| The settlement period to filter. This should be an integer from 1-50 inclusive. | [optional] 
 **bm_unit** | [**List[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **dataset** | [**List[str]**](str.md)| Datasets to filter. If omitted, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData.md)

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

# **balancing_dynamic_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData balancing_dynamic_get(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)

Dynamic Datasets Per-BMU

This endpoint provides the dynamic data for a requested BMU, excluding physical rate data.  It returns a \"snapshot\" of data valid at a given time, and optionally a time series of changes over a requested interval.                By default, all of the relevant datasets are returned: SIL, SEL, NDZ, NTB, NTO, MZT, MNZT, MDV, MDP.  The results from each dataset are transformed to a common response model, with the common integer field *Value*  mapped from the fields *Level*, *Period*, *Volume* or *Notice* in the original dataset, as relevant.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_dynamic_dynamic_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData
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
    api_instance = openapi_client.BalancingMechanismDynamicApi(api_client)
    bm_unit = '2__HFLEX001' # str | The BM Unit to query.
    snapshot_at = '2022-08-23T00:00Z' # datetime | When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset.
    until = '2022-08-24T00:00Z' # datetime | When to retrieve data until.  Data from the snapshot until this time will be returned. (optional)
    snapshot_at_settlement_period = 2 # int | The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. (optional)
    until_settlement_period = 2 # int | The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. (optional)
    dataset = ['[\"SEL\",\"MNZT\",\"MDP\"]'] # List[str] | Datasets to filter. If omitted, all datasets will be returned. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Dynamic Datasets Per-BMU
        api_response = api_instance.balancing_dynamic_get(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)
        print("The response of BalancingMechanismDynamicApi->balancing_dynamic_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingMechanismDynamicApi->balancing_dynamic_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **snapshot_at** | **datetime**| When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset. | 
 **until** | **datetime**| When to retrieve data until.  Data from the snapshot until this time will be returned. | [optional] 
 **snapshot_at_settlement_period** | **int**| The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. | [optional] 
 **until_settlement_period** | **int**| The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. | [optional] 
 **dataset** | [**List[str]**](str.md)| Datasets to filter. If omitted, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData.md)

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

# **balancing_dynamic_rates_all_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData balancing_dynamic_rates_all_get(settlement_date, settlement_period=settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)

Rate Datasets Market-Wide

This endpoint provides market-wide physical rate data, for all BMUs or a requested set of multiple BMUs.  It returns the data valid for a given settlement period. This includes a snapshot of data valid at the start  of the settlement period, and any changes published during that settlement period.                The settlement period to query can be specified as a date and settlement period, or as a datetime  which will resolve to the settlement period that time falls within.    By default, all of the relevant datasets are returned: RDRE, RURE, RDRI, RURI.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.    Some examples of date parameter combinations are shown below.                Filtering by datetime:                    /balancing/dynamic/rates/all?settlementDate=2023-01-18T01:00Z                Filtering by settlement date and period:                    /balancing/dynamic/rates/all?settlementDate=2023-01-18&settlementPeriod=3

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_dynamic_rate_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData
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
    api_instance = openapi_client.BalancingMechanismDynamicApi(api_client)
    settlement_date = '2022-09-01T00:00Z' # datetime | The settlement date or datetime to filter.
    settlement_period = 2 # int | The settlement period to filter. This should be an integer from 1-50 inclusive. (optional)
    bm_unit = ['[\"2__HFLEX001\",\"HUMR-1\"]'] # List[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
    dataset = ['[\"RURE\",\"RDRE\",\"RDRI\"]'] # List[str] | Datasets to return. If omitted, all datasets will be returned. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Rate Datasets Market-Wide
        api_response = api_instance.balancing_dynamic_rates_all_get(settlement_date, settlement_period=settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)
        print("The response of BalancingMechanismDynamicApi->balancing_dynamic_rates_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingMechanismDynamicApi->balancing_dynamic_rates_all_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **datetime**| The settlement date or datetime to filter. | 
 **settlement_period** | **int**| The settlement period to filter. This should be an integer from 1-50 inclusive. | [optional] 
 **bm_unit** | [**List[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **dataset** | [**List[str]**](str.md)| Datasets to return. If omitted, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData.md)

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

# **balancing_dynamic_rates_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData balancing_dynamic_rates_get(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)

Rate Datasets Per-BMU

This endpoint provides the physical rate data for a requested BMU.  It returns a \"snapshot\" of data valid at a given time, and optionally a time series of changes over a requested interval.                By default, all of the relevant datasets are returned: RDRE, RURE, RDRI, RURI.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_dynamic_rate_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData
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
    api_instance = openapi_client.BalancingMechanismDynamicApi(api_client)
    bm_unit = 'DRAXX-1' # str | The BM Unit to query.
    snapshot_at = '2022-09-01T00:00Z' # datetime | When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset.
    until = '2022-09-30T00:00Z' # datetime | When to retrieve data until.  Data from the snapshot until this time will be returned. (optional)
    snapshot_at_settlement_period = 2 # int | The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. (optional)
    until_settlement_period = 2 # int | The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. (optional)
    dataset = ['[\"RURE\",\"RDRE\",\"RDRI\"]'] # List[str] | Datasets to filter. If empty, all datasets will be returned. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Rate Datasets Per-BMU
        api_response = api_instance.balancing_dynamic_rates_get(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)
        print("The response of BalancingMechanismDynamicApi->balancing_dynamic_rates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancingMechanismDynamicApi->balancing_dynamic_rates_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **snapshot_at** | **datetime**| When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset. | 
 **until** | **datetime**| When to retrieve data until.  Data from the snapshot until this time will be returned. | [optional] 
 **snapshot_at_settlement_period** | **int**| The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. | [optional] 
 **until_settlement_period** | **int**| The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. | [optional] 
 **dataset** | [**List[str]**](str.md)| Datasets to filter. If empty, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData.md)

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

