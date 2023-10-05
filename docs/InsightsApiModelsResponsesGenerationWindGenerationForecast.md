# InsightsApiModelsResponsesGenerationWindGenerationForecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**generation** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_wind_generation_forecast import InsightsApiModelsResponsesGenerationWindGenerationForecast

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationWindGenerationForecast from a JSON string
insights_api_models_responses_generation_wind_generation_forecast_instance = InsightsApiModelsResponsesGenerationWindGenerationForecast.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationWindGenerationForecast.to_json()

# convert the object into a dict
insights_api_models_responses_generation_wind_generation_forecast_dict = insights_api_models_responses_generation_wind_generation_forecast_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationWindGenerationForecast from a dict
insights_api_models_responses_generation_wind_generation_forecast_form_dict = insights_api_models_responses_generation_wind_generation_forecast.from_dict(insights_api_models_responses_generation_wind_generation_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


