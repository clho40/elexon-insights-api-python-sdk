# InsightsApiModelsServiceDayAheadDemandForecastRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**boundary** | **str** |  | [optional] 
**transmission_system_demand** | **int** |  | [optional] 
**national_demand** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_service_day_ahead_demand_forecast_row import InsightsApiModelsServiceDayAheadDemandForecastRow

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsServiceDayAheadDemandForecastRow from a JSON string
insights_api_models_service_day_ahead_demand_forecast_row_instance = InsightsApiModelsServiceDayAheadDemandForecastRow.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsServiceDayAheadDemandForecastRow.to_json()

# convert the object into a dict
insights_api_models_service_day_ahead_demand_forecast_row_dict = insights_api_models_service_day_ahead_demand_forecast_row_instance.to_dict()
# create an instance of InsightsApiModelsServiceDayAheadDemandForecastRow from a dict
insights_api_models_service_day_ahead_demand_forecast_row_form_dict = insights_api_models_service_day_ahead_demand_forecast_row.from_dict(insights_api_models_service_day_ahead_demand_forecast_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


