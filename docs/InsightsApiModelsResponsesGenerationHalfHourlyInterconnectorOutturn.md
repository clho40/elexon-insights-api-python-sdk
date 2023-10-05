# InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] [readonly] 
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_date_timezone** | **str** |  | [optional] [readonly] 
**settlement_period** | **int** |  | [optional] 
**interconnector_name** | **str** |  | [optional] 
**generation** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_half_hourly_interconnector_outturn import InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn from a JSON string
insights_api_models_responses_generation_half_hourly_interconnector_outturn_instance = InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn.to_json()

# convert the object into a dict
insights_api_models_responses_generation_half_hourly_interconnector_outturn_dict = insights_api_models_responses_generation_half_hourly_interconnector_outturn_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn from a dict
insights_api_models_responses_generation_half_hourly_interconnector_outturn_form_dict = insights_api_models_responses_generation_half_hourly_interconnector_outturn.from_dict(insights_api_models_responses_generation_half_hourly_interconnector_outturn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


