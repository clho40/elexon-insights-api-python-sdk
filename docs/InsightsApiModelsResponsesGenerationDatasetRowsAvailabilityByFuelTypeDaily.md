# InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**fuel_type** | **str** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**system_zone** | **str** |  | [optional] 
**forecast_date** | **date** |  | [optional] 
**forecast_date_timezone** | **str** |  | [optional] [readonly] 
**output_usable** | **int** |  | [optional] 
**bidding_zone** | **str** |  | [optional] 
**interconnector_name** | **str** |  | [optional] 
**interconnector** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_daily import InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily from a JSON string
insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_daily_instance = InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily.to_json()

# convert the object into a dict
insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_daily_dict = insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_daily_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily from a dict
insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_daily_form_dict = insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_daily.from_dict(insights_api_models_responses_generation_dataset_rows_availability_by_fuel_type_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


