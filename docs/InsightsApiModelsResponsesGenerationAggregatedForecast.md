# InsightsApiModelsResponsesGenerationAggregatedForecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forecast_date** | **date** |  | [optional] 
**data** | [**List[InsightsApiModelsResponsesGenerationForecastFuelData]**](InsightsApiModelsResponsesGenerationForecastFuelData.md) |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_aggregated_forecast import InsightsApiModelsResponsesGenerationAggregatedForecast

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationAggregatedForecast from a JSON string
insights_api_models_responses_generation_aggregated_forecast_instance = InsightsApiModelsResponsesGenerationAggregatedForecast.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationAggregatedForecast.to_json()

# convert the object into a dict
insights_api_models_responses_generation_aggregated_forecast_dict = insights_api_models_responses_generation_aggregated_forecast_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationAggregatedForecast from a dict
insights_api_models_responses_generation_aggregated_forecast_form_dict = insights_api_models_responses_generation_aggregated_forecast.from_dict(insights_api_models_responses_generation_aggregated_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


