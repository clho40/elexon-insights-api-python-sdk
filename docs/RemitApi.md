# openapi_client.RemitApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_emit_get**](RemitApi.md#r_emit_get) | **GET** /REMIT | Remit bulk data by Message IDs
[**r_emit_list_by_event_get**](RemitApi.md#r_emit_list_by_event_get) | **GET** /REMIT/list/by-event | Remit list message identifiers by event
[**r_emit_list_by_event_stream_get**](RemitApi.md#r_emit_list_by_event_stream_get) | **GET** /REMIT/list/by-event/stream | Remit list message identifiers by event stream
[**r_emit_list_by_publish_get**](RemitApi.md#r_emit_list_by_publish_get) | **GET** /REMIT/list/by-publish | Remit list message identifiers by publish time
[**r_emit_list_by_publish_stream_get**](RemitApi.md#r_emit_list_by_publish_stream_get) | **GET** /REMIT/list/by-publish/stream | Remit list message identifiers by publish time stream
[**r_emit_message_id_get**](RemitApi.md#r_emit_message_id_get) | **GET** /REMIT/{messageId} | Remit data by Message ID
[**r_emit_revisions_get**](RemitApi.md#r_emit_revisions_get) | **GET** /REMIT/revisions | Remit message revisions by MRID or Message ID
[**r_emit_search_get**](RemitApi.md#r_emit_search_get) | **GET** /REMIT/search | Remit data by MRID


# **r_emit_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId r_emit_get(message_id, format=format)

Remit bulk data by Message IDs

This endpoint provides one or more REMIT messages based on the given Message IDs.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_remit_remit_message_with_id import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId
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
    api_instance = openapi_client.RemitApi(api_client)
    message_id = [[1,2,3,4]] # List[int] | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Remit bulk data by Message IDs
        api_response = api_instance.r_emit_get(message_id, format=format)
        print("The response of RemitApi->r_emit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | [**List[int]**](int.md)|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**404** | No data found for given query parameters |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_emit_list_by_event_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl r_emit_list_by_event_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only, format=format)

Remit list message identifiers by event

This endpoint provides a list of REMIT message identifiers based on the event start time, end time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_remit_remit_message_identifier_with_url import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl
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
    api_instance = openapi_client.RemitApi(api_client)
    var_from = '2023/04/13 07:00' # datetime | 
    to = '2023/04/14 07:00' # datetime | 
    participant_id = 'EECL' # str |  (optional)
    asset_id = 'T_RATSGT-2' # str |  (optional)
    message_type = 'UnavailabilitiesOfElectricityFacilities' # str |  (optional)
    unavailability_type = 'Planned' # str |  (optional)
    event_type = ['[\"Production Unavailability\",\"Transmission unavailability\"]'] # List[str] |  (optional)
    fuel_type = ['[\"Fossil Hard coal\",\"Biomass\"]'] # List[str] |  (optional)
    latest_revision_only = true # bool |  (optional)
    profile_only = false # bool |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Remit list message identifiers by event
        api_response = api_instance.r_emit_list_by_event_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only, format=format)
        print("The response of RemitApi->r_emit_list_by_event_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_list_by_event_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_emit_list_by_event_stream_get**
> List[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl] r_emit_list_by_event_stream_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only)

Remit list message identifiers by event stream

This endpoint provides a list of REMIT message identifiers based on the event start, end time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.                This endpoint has an optimised JSON payload and is aimed at frequent requests for the Remit list message identifiers data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_transparency_remit_remit_message_identifier_with_url import InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl
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
    api_instance = openapi_client.RemitApi(api_client)
    var_from = '2023/04/13 07:00' # datetime | 
    to = '2023/04/14 07:00' # datetime | 
    participant_id = 'EECL' # str |  (optional)
    asset_id = 'T_RATSGT-2' # str |  (optional)
    message_type = 'UnavailabilitiesOfElectricityFacilities' # str |  (optional)
    unavailability_type = 'Planned' # str |  (optional)
    event_type = ['[\"Production Unavailability\",\"Transmission unavailability\"]'] # List[str] |  (optional)
    fuel_type = ['[\"Fossil Hard coal\",\"Biomass\"]'] # List[str] |  (optional)
    latest_revision_only = true # bool |  (optional)
    profile_only = false # bool |  (optional)

    try:
        # Remit list message identifiers by event stream
        api_response = api_instance.r_emit_list_by_event_stream_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only)
        print("The response of RemitApi->r_emit_list_by_event_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_list_by_event_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 

### Return type

[**List[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl]**](InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

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

# **r_emit_list_by_publish_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl r_emit_list_by_publish_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only, format=format)

Remit list message identifiers by publish time

This endpoint provides a list of REMIT message identifiers based on the publish time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_remit_remit_message_identifier_with_url import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl
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
    api_instance = openapi_client.RemitApi(api_client)
    var_from = '2023/04/13 07:00' # datetime | 
    to = '2023/04/14 07:00' # datetime | 
    participant_id = 'EECL' # str |  (optional)
    asset_id = 'T_RATSGT-2' # str |  (optional)
    message_type = 'UnavailabilitiesOfElectricityFacilities' # str |  (optional)
    unavailability_type = 'Planned' # str |  (optional)
    event_type = ['[\"Production Unavailability\",\"Transmission unavailability\"]'] # List[str] |  (optional)
    fuel_type = ['[\"Fossil Hard coal\",\"Biomass\"]'] # List[str] |  (optional)
    latest_revision_only = true # bool |  (optional)
    profile_only = false # bool |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Remit list message identifiers by publish time
        api_response = api_instance.r_emit_list_by_publish_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only, format=format)
        print("The response of RemitApi->r_emit_list_by_publish_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_list_by_publish_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_emit_list_by_publish_stream_get**
> List[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl] r_emit_list_by_publish_stream_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only)

Remit list message identifiers by publish time stream

This endpoint provides a list of REMIT message identifiers based on the publish time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.                This endpoint has an optimised JSON payload and is aimed at frequent requests for the Remit list message identifiers data.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_transparency_remit_remit_message_identifier_with_url import InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl
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
    api_instance = openapi_client.RemitApi(api_client)
    var_from = '2023/04/13 07:00' # datetime | 
    to = '2023/04/14 07:00' # datetime | 
    participant_id = 'EECL' # str |  (optional)
    asset_id = 'T_RATSGT-2' # str |  (optional)
    message_type = 'UnavailabilitiesOfElectricityFacilities' # str |  (optional)
    unavailability_type = 'Planned' # str |  (optional)
    event_type = ['[\"Production Unavailability\",\"Transmission unavailability\"]'] # List[str] |  (optional)
    fuel_type = ['[\"Fossil Hard coal\",\"Biomass\"]'] # List[str] |  (optional)
    latest_revision_only = true # bool |  (optional)
    profile_only = false # bool |  (optional)

    try:
        # Remit list message identifiers by publish time stream
        api_response = api_instance.r_emit_list_by_publish_stream_get(var_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only)
        print("The response of RemitApi->r_emit_list_by_publish_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_list_by_publish_stream_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**List[str]**](str.md)|  | [optional] 
 **fuel_type** | [**List[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 

### Return type

[**List[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl]**](InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

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

# **r_emit_message_id_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId r_emit_message_id_get(message_id, format=format)

Remit data by Message ID

This endpoint provides a REMIT message based on a given Message ID.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_remit_remit_message_with_id import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId
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
    api_instance = openapi_client.RemitApi(api_client)
    message_id = 56 # int | 
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Remit data by Message ID
        api_response = api_instance.r_emit_message_id_get(message_id, format=format)
        print("The response of RemitApi->r_emit_message_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_message_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**404** | No data found for given id |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_emit_revisions_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl r_emit_revisions_get(mrid=mrid, message_id=message_id, format=format)

Remit message revisions by MRID or Message ID

This endpoint provides all of the REMIT Message Revisions for a given Message Group.  The Message Group can be specified in two ways:  - via an MRID which specifies a unique Message Group  - via a Message ID, as each Message will belong to a unique Message Group

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_remit_remit_message_identifier_with_url import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl
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
    api_instance = openapi_client.RemitApi(api_client)
    mrid = '48X000000000080X-NGET-RMT-00014669' # str |  (optional)
    message_id = 1 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Remit message revisions by MRID or Message ID
        api_response = api_instance.r_emit_revisions_get(mrid=mrid, message_id=message_id, format=format)
        print("The response of RemitApi->r_emit_revisions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_revisions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mrid** | **str**|  | [optional] 
 **message_id** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**404** | No data found for given query parameters |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_emit_search_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId r_emit_search_get(mrid, revision_number=revision_number, format=format)

Remit data by MRID

This endpoint provides one or more REMIT messages based on the given MRID and revision number. If none is given  it returns the REMIT message with the latest revision number.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_transparency_remit_remit_message_with_id import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId
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
    api_instance = openapi_client.RemitApi(api_client)
    mrid = '48X000000000080X-NGET-RMT-00014669' # str | 
    revision_number = 56 # int |  (optional)
    format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

    try:
        # Remit data by MRID
        api_response = api_instance.r_emit_search_get(mrid, revision_number=revision_number, format=format)
        print("The response of RemitApi->r_emit_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemitApi->r_emit_search_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mrid** | **str**|  | 
 **revision_number** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved |  -  |
**400** | Error with query parameters - see response for details |  -  |
**404** | No data found for given query parameters |  -  |
**500** | Server error - please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

