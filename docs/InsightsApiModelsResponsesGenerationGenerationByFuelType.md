# InsightsApiModelsResponsesGenerationGenerationByFuelType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] [readonly] 
**fuel_type** | **str** |  | [optional] 
**current_usage** | **int** |  | [optional] 
**current_percentage** | **float** |  | [optional] 
**half_hour_usage** | **int** |  | [optional] 
**half_hour_percentage** | **float** |  | [optional] 
**twenty_four_hour_usage** | **int** |  | [optional] 
**twenty_four_hour_percentage** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_generation_by_fuel_type import InsightsApiModelsResponsesGenerationGenerationByFuelType

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationGenerationByFuelType from a JSON string
insights_api_models_responses_generation_generation_by_fuel_type_instance = InsightsApiModelsResponsesGenerationGenerationByFuelType.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationGenerationByFuelType.to_json()

# convert the object into a dict
insights_api_models_responses_generation_generation_by_fuel_type_dict = insights_api_models_responses_generation_generation_by_fuel_type_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationGenerationByFuelType from a dict
insights_api_models_responses_generation_generation_by_fuel_type_form_dict = insights_api_models_responses_generation_generation_by_fuel_type.from_dict(insights_api_models_responses_generation_generation_by_fuel_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


