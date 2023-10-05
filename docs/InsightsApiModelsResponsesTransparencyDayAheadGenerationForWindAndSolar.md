# InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**process_type** | **str** |  | [optional] 
**business_type** | **str** |  | [optional] 
**psr_type** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar import InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar from a JSON string
insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar_instance = InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar.to_json()

# convert the object into a dict
insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar_dict = insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar_instance.to_dict()
# create an instance of InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar from a dict
insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar_form_dict = insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar.from_dict(insights_api_models_responses_transparency_day_ahead_generation_for_wind_and_solar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


