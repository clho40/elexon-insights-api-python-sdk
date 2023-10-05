# InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**transmission_system_demand** | **int** |  | [optional] 
**national_demand** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**boundary** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_demand_forecast_demand_forecast_day_ahead import InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead from a JSON string
insights_api_models_responses_demand_forecast_demand_forecast_day_ahead_instance = InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.to_json()

# convert the object into a dict
insights_api_models_responses_demand_forecast_demand_forecast_day_ahead_dict = insights_api_models_responses_demand_forecast_demand_forecast_day_ahead_instance.to_dict()
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead from a dict
insights_api_models_responses_demand_forecast_demand_forecast_day_ahead_form_dict = insights_api_models_responses_demand_forecast_demand_forecast_day_ahead.from_dict(insights_api_models_responses_demand_forecast_demand_forecast_day_ahead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


