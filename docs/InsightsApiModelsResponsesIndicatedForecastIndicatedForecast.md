# InsightsApiModelsResponsesIndicatedForecastIndicatedForecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**boundary** | **str** |  | [optional] 
**indicated_generation** | **int** |  | [optional] 
**indicated_demand** | **int** |  | [optional] 
**indicated_margin** | **int** |  | [optional] 
**indicated_imbalance** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_indicated_forecast_indicated_forecast import InsightsApiModelsResponsesIndicatedForecastIndicatedForecast

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesIndicatedForecastIndicatedForecast from a JSON string
insights_api_models_responses_indicated_forecast_indicated_forecast_instance = InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.to_json()

# convert the object into a dict
insights_api_models_responses_indicated_forecast_indicated_forecast_dict = insights_api_models_responses_indicated_forecast_indicated_forecast_instance.to_dict()
# create an instance of InsightsApiModelsResponsesIndicatedForecastIndicatedForecast from a dict
insights_api_models_responses_indicated_forecast_indicated_forecast_form_dict = insights_api_models_responses_indicated_forecast_indicated_forecast.from_dict(insights_api_models_responses_indicated_forecast_indicated_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


