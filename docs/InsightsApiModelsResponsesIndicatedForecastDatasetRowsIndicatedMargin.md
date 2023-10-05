# InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**margin** | **int** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**boundary** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_indicated_forecast_dataset_rows_indicated_margin import InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin from a JSON string
insights_api_models_responses_indicated_forecast_dataset_rows_indicated_margin_instance = InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin.to_json()

# convert the object into a dict
insights_api_models_responses_indicated_forecast_dataset_rows_indicated_margin_dict = insights_api_models_responses_indicated_forecast_dataset_rows_indicated_margin_instance.to_dict()
# create an instance of InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin from a dict
insights_api_models_responses_indicated_forecast_dataset_rows_indicated_margin_form_dict = insights_api_models_responses_indicated_forecast_dataset_rows_indicated_margin.from_dict(insights_api_models_responses_indicated_forecast_dataset_rows_indicated_margin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


