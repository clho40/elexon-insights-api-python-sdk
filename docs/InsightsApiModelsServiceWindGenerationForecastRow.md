# InsightsApiModelsServiceWindGenerationForecastRow


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
from openapi_client.models.insights_api_models_service_wind_generation_forecast_row import InsightsApiModelsServiceWindGenerationForecastRow

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsServiceWindGenerationForecastRow from a JSON string
insights_api_models_service_wind_generation_forecast_row_instance = InsightsApiModelsServiceWindGenerationForecastRow.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsServiceWindGenerationForecastRow.to_json()

# convert the object into a dict
insights_api_models_service_wind_generation_forecast_row_dict = insights_api_models_service_wind_generation_forecast_row_instance.to_dict()
# create an instance of InsightsApiModelsServiceWindGenerationForecastRow from a dict
insights_api_models_service_wind_generation_forecast_row_form_dict = insights_api_models_service_wind_generation_forecast_row.from_dict(insights_api_models_service_wind_generation_forecast_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


