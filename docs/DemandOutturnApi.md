# openapi_client.DemandOutturnApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demand_get**](DemandOutturnApi.md#demand_get) | **GET** /demand | Initial National Demand Outturn
[**demand_outturn_daily_get**](DemandOutturnApi.md#demand_outturn_daily_get) | **GET** /demand/outturn/daily | Initial National Demand Outturn Daily (INDOD)
[**demand_outturn_daily_stream_get**](DemandOutturnApi.md#demand_outturn_daily_stream_get) | **GET** /demand/outturn/daily/stream | Initial National Demand Outturn Daily (INDOD) stream
[**demand_peak_get**](DemandOutturnApi.md#demand_peak_get) | **GET** /demand/peak | Retrieve peak demand data for each day, based on ITSDO data
[**demand_peak_indicative_get**](DemandOutturnApi.md#demand_peak_indicative_get) | **GET** /demand/peak/indicative | Indicative Demand Peaks
[**demand_peak_indicative_operational_triad_season_get**](DemandOutturnApi.md#demand_peak_indicative_operational_triad_season_get) | **GET** /demand/peak/indicative/operational/{triadSeason} | Operational Data Demand Peak from a Triad Season
[**demand_peak_indicative_settlement_triad_season_get**](DemandOutturnApi.md#demand_peak_indicative_settlement_triad_season_get) | **GET** /demand/peak/indicative/settlement/{triadSeason} | Settlement Data Demand Peak from a Triad Season
[**demand_peak_triad_get**](DemandOutturnApi.md#demand_peak_triad_get) | **GET** /demand/peak/triad | Triad Demand Peaks
[**demand_rolling_system_demand_get**](DemandOutturnApi.md#demand_rolling_system_demand_get) | **GET** /demand/rollingSystemDemand | Rolling System Demand (ROLSYSDEM)
[**demand_stream_get**](DemandOutturnApi.md#demand_stream_get) | **GET** /demand/stream | Initial National Demand Outturn Stream
[**demand_summary_get**](DemandOutturnApi.md#demand_summary_get) | **GET** /demand/summary | System Demand Summary


# **demand_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn demand_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, format=format)

Initial National Demand Outturn

This endpoint provides data for Initial National Demand Outturn, which measures the  half-hour average MW demand metered by the Transmission Company based on its operational metering.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period. The data is represented with:  - INDO (Initial National Demand Outturn) which takes into account transmission losses but does not include station transformer load, pumped storage demand or interconnector demand.  - ITSDO (Initial Transmission System Demand Outturn) which takes into account transmission losses, station transformer load, pumped storage demand and interconnector demand.                This endpoint is useful for ad-hoc querying of the initial national demand outturn data.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_demand_outturn import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    settlement_date_from = '2022-09-20' # date | The settlement date from for the filter. This must be in the format yyyy-MM-dd. (optional)
    settlement_date_to = '2022-09-21' # date | The settlement date to for the filter. This must be in the format yyyy-MM-dd. (optional)
    settlement_period = [1] # List[int] |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Initial National Demand Outturn
        api_response = api_instance.demand_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, format=format)
        print("The response of DemandOutturnApi->demand_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| The settlement date from for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| The settlement date to for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**List[int]**](int.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)

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

# **demand_outturn_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow demand_outturn_daily_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, format=format)

Initial National Demand Outturn Daily (INDOD)

This endpoint provides initial National Demand outturn daily data. The total daily energy volume is the total  demand volume for the previous day expressed on an Initial National Demand Outturn (INDO) basis, i.e. excluding  station transformer, pumping and interconnector export demand. It is calculated from summing the half hourly  INDO demands (divided by two to convert to MWh).                If no date window is chosen, the search will default to results from the last 31 days.    This API endpoint has a maximum range of 2 years (731 days).

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_indod_row import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    settlement_date_from = '2023-08-26' # date |  (optional)
    settlement_date_to = '2023-08-27' # date |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Initial National Demand Outturn Daily (INDOD)
        api_response = api_instance.demand_outturn_daily_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, format=format)
        print("The response of DemandOutturnApi->demand_outturn_daily_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_outturn_daily_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**|  | [optional] 
 **settlement_date_to** | **date**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow.md)

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

# **demand_outturn_daily_stream_get**
> List[InsightsApiModelsResponsesDemandOutturnIndodRow] demand_outturn_daily_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to)

Initial National Demand Outturn Daily (INDOD) stream

This endpoint provides initial National Demand outturn daily data. The total daily energy volume is the total  demand volume for the previous day expressed on an Initial National Demand Outturn (INDO) basis, i.e. excluding  station transformer, pumping and interconnector export demand. It is calculated from summing the half hourly  INDO demands (divided by two to convert to MWh).                If no date window is chosen, the search will default to results from the last 31 days.    This endpoint has an optimised JSON payload and is aimed at frequent requests for the data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_demand_outturn_indod_row import InsightsApiModelsResponsesDemandOutturnIndodRow
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    settlement_date_from = '2023-08-26' # date |  (optional)
    settlement_date_to = '2023-08-27' # date |  (optional)

    try:
        # Initial National Demand Outturn Daily (INDOD) stream
        api_response = api_instance.demand_outturn_daily_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to)
        print("The response of DemandOutturnApi->demand_outturn_daily_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_outturn_daily_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**|  | [optional] 
 **settlement_date_to** | **date**|  | [optional] 

### Return type

[**List[InsightsApiModelsResponsesDemandOutturnIndodRow]**](InsightsApiModelsResponsesDemandOutturnIndodRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_peak_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak demand_peak_get(var_from=var_from, to=to, format=format)

Retrieve peak demand data for each day, based on ITSDO data

This endpoint allows for retrieving peak ITSDO demand for each day from National Grid ESO.  Results are filtered by a range of Date parameters.  Results default to yesterday's peak if no parameters are supplied.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_demand_outturn_peak import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    var_from = '2021-10-01' # date | The start of the requested date range. (optional)
    to = '2021-10-30' # date | The end of the requested date range. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Retrieve peak demand data for each day, based on ITSDO data
        api_response = api_instance.demand_peak_get(var_from=var_from, to=to, format=format)
        print("The response of DemandOutturnApi->demand_peak_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_peak_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.md)

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

# **demand_peak_indicative_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_indicative_get(data, triad_season_start_year=triad_season_start_year, var_from=var_from, to=to, format=format)

Indicative Demand Peaks

Indicative Demand Peaks using Operational Metering data are daily maxima values determined from  ITSDO and FUELHH data used to determine and visualise Triad.                Indicative Demand Peaks using Settlement Metering data are daily maxima values determined from  metered volume data from the S0142_bpi file. These peaks are not used for Triad visualisation as  they are always calculated based on the latest run type. Triads for settlement data  remain static after the National Grid report posted at the beginning of April after the Triad season has ended.                 If no filters are supplied, results default to the latest or current Triad season.  To specify a custom filter, you can supplier EITHER a Triad season start year, OR a date range, but not both.  If a Triad Season Start year is supplied, data for the Triad season beginning on 1 November  of the specified year will be returned.  If a date range is supplied, data will be returned for settlement dates within the date range inclusively.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_indicative_demand_peak import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    data = 'operational' # str | The type of data. Supports values of 'operational' or 'settlement'.
    triad_season_start_year = 56 # int | A year indicating the Triad season starting on 1 November of the given year, e.g. 2021. (optional)
    var_from = '2021-10-01' # date | The start of the requested date range. (optional)
    to = '2021-10-30' # date | The end of the requested date range. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Indicative Demand Peaks
        api_response = api_instance.demand_peak_indicative_get(data, triad_season_start_year=triad_season_start_year, var_from=var_from, to=to, format=format)
        print("The response of DemandOutturnApi->demand_peak_indicative_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_peak_indicative_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| The type of data. Supports values of &#39;operational&#39; or &#39;settlement&#39;. | 
 **triad_season_start_year** | **int**| A year indicating the Triad season starting on 1 November of the given year, e.g. 2021. | [optional] 
 **var_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

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

# **demand_peak_indicative_operational_triad_season_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_indicative_operational_triad_season_get(triad_season, format=format)

Operational Data Demand Peak from a Triad Season

Provides indicative demand peak data for a Triad season ITSDO and FUELHH files over a Triad season. For non-Triad  season dates please use the `peak/indicative` endpoint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_indicative_demand_peak import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    triad_season = 2021 # int | A year indicating the Triad season starting on 1 November of the given year
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Operational Data Demand Peak from a Triad Season
        api_response = api_instance.demand_peak_indicative_operational_triad_season_get(triad_season, format=format)
        print("The response of DemandOutturnApi->demand_peak_indicative_operational_triad_season_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_peak_indicative_operational_triad_season_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triad_season** | **int**| A year indicating the Triad season starting on 1 November of the given year | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

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

# **demand_peak_indicative_settlement_triad_season_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_indicative_settlement_triad_season_get(triad_season, format=format)

Settlement Data Demand Peak from a Triad Season

Provides indicative demand peak data for a Triad season from S0142_bpi files that were calculated  during the Triad season. For the data from the latest settlement runs for the Triad season use the  `peak/indicative` endpoint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_indicative_demand_peak import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    triad_season = 2021 # int | A year indicating the Triad season starting on 1 November of the given year
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Settlement Data Demand Peak from a Triad Season
        api_response = api_instance.demand_peak_indicative_settlement_triad_season_get(triad_season, format=format)
        print("The response of DemandOutturnApi->demand_peak_indicative_settlement_triad_season_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_peak_indicative_settlement_triad_season_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triad_season** | **int**| A year indicating the Triad season starting on 1 November of the given year | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

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

# **demand_peak_triad_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_triad_get(data, triad_season_start_year=triad_season_start_year, format=format)

Triad Demand Peaks

Operational Triad peaks are calculated from the indicative demand peaks data.    Settlement Triad Peaks are calculated from the latest metered volume data available at the point one month following the Triad season's end.  For any Triad season still in progress, the latest run type data is used.                All Triad peaks are at least 10 days clear of one another.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_indicative_demand_peak import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    data = 'operational' # str | The type of data. Supports values of 'operational' or 'settlement'.
    triad_season_start_year = 2021 # int | A year indicating the Triad season starting on 1 November of the given year. (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Triad Demand Peaks
        api_response = api_instance.demand_peak_triad_get(data, triad_season_start_year=triad_season_start_year, format=format)
        print("The response of DemandOutturnApi->demand_peak_triad_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_peak_triad_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| The type of data. Supports values of &#39;operational&#39; or &#39;settlement&#39;. | 
 **triad_season_start_year** | **int**| A year indicating the Triad season starting on 1 November of the given year. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

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

# **demand_rolling_system_demand_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand demand_rolling_system_demand_get(var_from=var_from, to=to, format=format)

Rolling System Demand (ROLSYSDEM)

This endpoint provides the Rolling System Data and this is derived from the total  of all Fuel Type categories from the Generation by Fuel Type report.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_rolling_system_demand import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Rolling System Demand (ROLSYSDEM)
        api_response = api_instance.demand_rolling_system_demand_get(var_from=var_from, to=to, format=format)
        print("The response of DemandOutturnApi->demand_rolling_system_demand_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_rolling_system_demand_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)

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

# **demand_stream_get**
> List[InsightsApiModelsResponsesDemandOutturnDemandOutturn] demand_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period)

Initial National Demand Outturn Stream

This endpoint provides data for Initial National Demand Outturn, which measures the  half-hour average MW demand metered by the Transmission Company based on its operational metering.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period. The data is represented with:  - INDO (Initial National Demand Outturn) which takes into account transmission losses but does not include station transformer load, pumped storage demand or interconnector demand.  - ITSDO (Initial Transmission System Demand Outturn) which takes into account transmission losses, station transformer load, pumped storage demand and interconnector demand.                This endpoint has an optimised JSON payload and is aimed at frequent requests for the initial national demand outturn data.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_demand_outturn_demand_outturn import InsightsApiModelsResponsesDemandOutturnDemandOutturn
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    settlement_date_from = '2022-09-20' # date | The settlement date from for the filter. This must be in the format yyyy-MM-dd. (optional)
    settlement_date_to = '2022-09-21' # date | The settlement date to for the filter. This must be in the format yyyy-MM-dd. (optional)
    settlement_period = [1] # List[int] |  (optional)

    try:
        # Initial National Demand Outturn Stream
        api_response = api_instance.demand_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period)
        print("The response of DemandOutturnApi->demand_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| The settlement date from for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| The settlement date to for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**List[InsightsApiModelsResponsesDemandOutturnDemandOutturn]**](InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_summary_get**
> List[InsightsApiModelsResponsesDemandOutturnRollingSystemDemand] demand_summary_get(var_from=var_from, to=to, format=format)

System Demand Summary

⚠ This endpoint provides a down-sampled data summary intended for visualisation purposes.  Use datasets endpoints for full dataset access.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_demand_outturn_rolling_system_demand import InsightsApiModelsResponsesDemandOutturnRollingSystemDemand
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
    api_instance = openapi_client.DemandOutturnApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # System Demand Summary
        api_response = api_instance.demand_summary_get(var_from=var_from, to=to, format=format)
        print("The response of DemandOutturnApi->demand_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemandOutturnApi->demand_summary_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**List[InsightsApiModelsResponsesDemandOutturnRollingSystemDemand]**](InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)

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

