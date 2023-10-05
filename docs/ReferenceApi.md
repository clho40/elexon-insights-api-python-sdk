# openapi_client.ReferenceApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reference_bmunits_all_get**](ReferenceApi.md#reference_bmunits_all_get) | **GET** /reference/bmunits/all | BM Units and Mappings
[**reference_fueltypes_all_get**](ReferenceApi.md#reference_fueltypes_all_get) | **GET** /reference/fueltypes/all | Fuel Types
[**reference_interconnectors_all_get**](ReferenceApi.md#reference_interconnectors_all_get) | **GET** /reference/interconnectors/all | Interconnectors
[**reference_remit_assets_all_get**](ReferenceApi.md#reference_remit_assets_all_get) | **GET** /reference/remit/assets/all | Assets
[**reference_remit_fueltypes_all_get**](ReferenceApi.md#reference_remit_fueltypes_all_get) | **GET** /reference/remit/fueltypes/all | Remit Fuel Types
[**reference_remit_participants_all_get**](ReferenceApi.md#reference_remit_participants_all_get) | **GET** /reference/remit/participants/all | Participants


# **reference_bmunits_all_get**
> List[InsightsApiModelsResponsesReferenceBmUnitData] reference_bmunits_all_get()

BM Units and Mappings

This endpoint provides a current list of BM units and mappings held by Elexon

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_reference_bm_unit_data import InsightsApiModelsResponsesReferenceBmUnitData
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
    api_instance = openapi_client.ReferenceApi(api_client)

    try:
        # BM Units and Mappings
        api_response = api_instance.reference_bmunits_all_get()
        print("The response of ReferenceApi->reference_bmunits_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->reference_bmunits_all_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[InsightsApiModelsResponsesReferenceBmUnitData]**](InsightsApiModelsResponsesReferenceBmUnitData.md)

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

# **reference_fueltypes_all_get**
> List[str] reference_fueltypes_all_get()

Fuel Types

This endpoint provides a current list of FuelTypes

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ReferenceApi(api_client)

    try:
        # Fuel Types
        api_response = api_instance.reference_fueltypes_all_get()
        print("The response of ReferenceApi->reference_fueltypes_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->reference_fueltypes_all_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **reference_interconnectors_all_get**
> List[InsightsApiModelsResponsesReferenceInterconnectorData] reference_interconnectors_all_get()

Interconnectors

This endpoint provides a current list of Interconnectors

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_reference_interconnector_data import InsightsApiModelsResponsesReferenceInterconnectorData
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
    api_instance = openapi_client.ReferenceApi(api_client)

    try:
        # Interconnectors
        api_response = api_instance.reference_interconnectors_all_get()
        print("The response of ReferenceApi->reference_interconnectors_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->reference_interconnectors_all_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[InsightsApiModelsResponsesReferenceInterconnectorData]**](InsightsApiModelsResponsesReferenceInterconnectorData.md)

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

# **reference_remit_assets_all_get**
> List[str] reference_remit_assets_all_get()

Assets

This endpoint provides a current list of AssetIds received from REMIT messages

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ReferenceApi(api_client)

    try:
        # Assets
        api_response = api_instance.reference_remit_assets_all_get()
        print("The response of ReferenceApi->reference_remit_assets_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->reference_remit_assets_all_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **reference_remit_fueltypes_all_get**
> List[str] reference_remit_fueltypes_all_get()

Remit Fuel Types

This endpoint provides a current list of fuel types received from REMIT messages

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ReferenceApi(api_client)

    try:
        # Remit Fuel Types
        api_response = api_instance.reference_remit_fueltypes_all_get()
        print("The response of ReferenceApi->reference_remit_fueltypes_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->reference_remit_fueltypes_all_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **reference_remit_participants_all_get**
> List[str] reference_remit_participants_all_get()

Participants

This endpoint provides a current list of ParticipantIds received from REMIT messages

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ReferenceApi(api_client)

    try:
        # Participants
        api_response = api_instance.reference_remit_participants_all_get()
        print("The response of ReferenceApi->reference_remit_participants_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->reference_remit_participants_all_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

