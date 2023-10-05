# InsightsApiModelsResponsesDemandForecastDemandForecastWeekly


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**transmission_system_demand** | **int** |  | [optional] 
**national_demand** | **int** |  | [optional] 
**forecast_week** | **int** |  | [optional] 
**forecast_year** | **int** |  | [optional] 
**week_start_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_demand_forecast_demand_forecast_weekly import InsightsApiModelsResponsesDemandForecastDemandForecastWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastWeekly from a JSON string
insights_api_models_responses_demand_forecast_demand_forecast_weekly_instance = InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.to_json()

# convert the object into a dict
insights_api_models_responses_demand_forecast_demand_forecast_weekly_dict = insights_api_models_responses_demand_forecast_demand_forecast_weekly_instance.to_dict()
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastWeekly from a dict
insights_api_models_responses_demand_forecast_demand_forecast_weekly_form_dict = insights_api_models_responses_demand_forecast_demand_forecast_weekly.from_dict(insights_api_models_responses_demand_forecast_demand_forecast_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


