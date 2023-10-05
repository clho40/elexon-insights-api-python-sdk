# InsightsApiModelsResponsesDemandForecastDemandForecastPeak


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**boundary** | **str** |  | [optional] 
**transmission_system_demand** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_demand_forecast_demand_forecast_peak import InsightsApiModelsResponsesDemandForecastDemandForecastPeak

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastPeak from a JSON string
insights_api_models_responses_demand_forecast_demand_forecast_peak_instance = InsightsApiModelsResponsesDemandForecastDemandForecastPeak.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesDemandForecastDemandForecastPeak.to_json()

# convert the object into a dict
insights_api_models_responses_demand_forecast_demand_forecast_peak_dict = insights_api_models_responses_demand_forecast_demand_forecast_peak_instance.to_dict()
# create an instance of InsightsApiModelsResponsesDemandForecastDemandForecastPeak from a dict
insights_api_models_responses_demand_forecast_demand_forecast_peak_form_dict = insights_api_models_responses_demand_forecast_demand_forecast_peak.from_dict(insights_api_models_responses_demand_forecast_demand_forecast_peak_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


