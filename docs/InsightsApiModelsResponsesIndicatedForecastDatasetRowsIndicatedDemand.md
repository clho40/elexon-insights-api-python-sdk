# InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**demand** | **int** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**boundary** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_indicated_forecast_dataset_rows_indicated_demand import InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand from a JSON string
insights_api_models_responses_indicated_forecast_dataset_rows_indicated_demand_instance = InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.to_json()

# convert the object into a dict
insights_api_models_responses_indicated_forecast_dataset_rows_indicated_demand_dict = insights_api_models_responses_indicated_forecast_dataset_rows_indicated_demand_instance.to_dict()
# create an instance of InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand from a dict
insights_api_models_responses_indicated_forecast_dataset_rows_indicated_demand_form_dict = insights_api_models_responses_indicated_forecast_dataset_rows_indicated_demand.from_dict(insights_api_models_responses_indicated_forecast_dataset_rows_indicated_demand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


