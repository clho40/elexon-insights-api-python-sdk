# InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**fuel_type** | **str** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**system_zone** | **str** |  | [optional] 
**calendar_week_number** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**output_usable** | **int** |  | [optional] 
**bidding_zone** | **str** |  | [optional] 
**interconnector_name** | **str** |  | [optional] 
**interconnector** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_weekly import InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly from a JSON string
insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_weekly_instance = InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly.to_json()

# convert the object into a dict
insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_weekly_dict = insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_weekly_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly from a dict
insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_weekly_form_dict = insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_weekly.from_dict(insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


