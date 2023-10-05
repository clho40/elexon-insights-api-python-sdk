# InsightsApiModelsResponsesForecastMarginForecastMarginWeekly


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**margin** | **int** |  | [optional] 
**week** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**week_start_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_forecast_margin_forecast_margin_weekly import InsightsApiModelsResponsesForecastMarginForecastMarginWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesForecastMarginForecastMarginWeekly from a JSON string
insights_api_models_responses_forecast_margin_forecast_margin_weekly_instance = InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.to_json()

# convert the object into a dict
insights_api_models_responses_forecast_margin_forecast_margin_weekly_dict = insights_api_models_responses_forecast_margin_forecast_margin_weekly_instance.to_dict()
# create an instance of InsightsApiModelsResponsesForecastMarginForecastMarginWeekly from a dict
insights_api_models_responses_forecast_margin_forecast_margin_weekly_form_dict = insights_api_models_responses_forecast_margin_forecast_margin_weekly.from_dict(insights_api_models_responses_forecast_margin_forecast_margin_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


