# InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**mrid** | **str** |  | [optional] 
**revision_number** | **int** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**message_type** | **str** |  | [optional] 
**message_heading** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**unavailability_type** | **str** |  | [optional] 
**participant_id** | **str** |  | [optional] 
**registration_code** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**asset_type** | **str** |  | [optional] 
**affected_unit** | **str** |  | [optional] 
**affected_unit_eic** | **str** |  | [optional] 
**affected_area** | **str** |  | [optional] 
**bidding_zone** | **str** |  | [optional] 
**fuel_type** | **str** |  | [optional] 
**normal_capacity** | **float** |  | [optional] 
**available_capacity** | **float** |  | [optional] 
**unavailable_capacity** | **float** |  | [optional] 
**event_status** | **str** |  | [optional] 
**event_start_time** | **datetime** |  | [optional] 
**event_end_time** | **datetime** |  | [optional] 
**duration_uncertainty** | **str** |  | [optional] 
**cause** | **str** |  | [optional] 
**related_information** | **str** |  | [optional] 
**outage_profile** | [**List[InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData]**](InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_transparency_remit_remit_message_with_id import InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId from a JSON string
insights_api_models_responses_transparency_remit_remit_message_with_id_instance = InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.to_json()

# convert the object into a dict
insights_api_models_responses_transparency_remit_remit_message_with_id_dict = insights_api_models_responses_transparency_remit_remit_message_with_id_instance.to_dict()
# create an instance of InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId from a dict
insights_api_models_responses_transparency_remit_remit_message_with_id_form_dict = insights_api_models_responses_transparency_remit_remit_message_with_id.from_dict(insights_api_models_responses_transparency_remit_remit_message_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


