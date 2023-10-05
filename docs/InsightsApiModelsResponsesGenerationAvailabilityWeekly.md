# InsightsApiModelsResponsesGenerationAvailabilityWeekly


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**fuel_type** | **str** |  | [optional] 
**ngc_bm_unit** | **str** |  | [optional] 
**output_usable** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**calendar_week_number** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_availability_weekly import InsightsApiModelsResponsesGenerationAvailabilityWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationAvailabilityWeekly from a JSON string
insights_api_models_responses_generation_availability_weekly_instance = InsightsApiModelsResponsesGenerationAvailabilityWeekly.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationAvailabilityWeekly.to_json()

# convert the object into a dict
insights_api_models_responses_generation_availability_weekly_dict = insights_api_models_responses_generation_availability_weekly_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationAvailabilityWeekly from a dict
insights_api_models_responses_generation_availability_weekly_form_dict = insights_api_models_responses_generation_availability_weekly.from_dict(insights_api_models_responses_generation_availability_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


