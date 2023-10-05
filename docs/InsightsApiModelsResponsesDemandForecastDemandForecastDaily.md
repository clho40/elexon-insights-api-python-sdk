# InsightsApiModelsResponsesDemandForecastDemandForecastDaily


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**transmission_system_demand** | **int** |  | [optional] 
**national_demand** | **int** |  | [optional] 
**forecast_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_demand_forecast_demand_forecast_daily import InsightsApiModelsResponsesDemandForecastDemandForecastDaily

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastDaily from a JSON string
insights_api_models_responses_demand_forecast_demand_forecast_daily_instance = InsightsApiModelsResponsesDemandForecastDemandForecastDaily.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesDemandForecastDemandForecastDaily.to_json()

# convert the object into a dict
insights_api_models_responses_demand_forecast_demand_forecast_daily_dict = insights_api_models_responses_demand_forecast_demand_forecast_daily_instance.to_dict()
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastDaily from a dict
insights_api_models_responses_demand_forecast_demand_forecast_daily_form_dict = insights_api_models_responses_demand_forecast_demand_forecast_daily.from_dict(insights_api_models_responses_demand_forecast_demand_forecast_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


