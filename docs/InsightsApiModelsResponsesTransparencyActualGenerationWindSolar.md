# InsightsApiModelsResponsesTransparencyActualGenerationWindSolar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**business_type** | **str** |  | [optional] 
**psr_type** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_transparency_actual_generation_wind_solar import InsightsApiModelsResponsesTransparencyActualGenerationWindSolar

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesTransparencyActualGenerationWindSolar from a JSON string
insights_api_models_responses_transparency_actual_generation_wind_solar_instance = InsightsApiModelsResponsesTransparencyActualGenerationWindSolar.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesTransparencyActualGenerationWindSolar.to_json()

# convert the object into a dict
insights_api_models_responses_transparency_actual_generation_wind_solar_dict = insights_api_models_responses_transparency_actual_generation_wind_solar_instance.to_dict()
# create an instance of InsightsApiModelsResponsesTransparencyActualGenerationWindSolar from a dict
insights_api_models_responses_transparency_actual_generation_wind_solar_form_dict = insights_api_models_responses_transparency_actual_generation_wind_solar.from_dict(insights_api_models_responses_transparency_actual_generation_wind_solar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


