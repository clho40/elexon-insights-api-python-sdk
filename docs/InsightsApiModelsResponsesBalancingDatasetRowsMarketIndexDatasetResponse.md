# InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**data_provider** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**price** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dataset_rows_market_index_dataset_response import InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse from a JSON string
insights_api_models_responses_balancing_dataset_rows_market_index_dataset_response_instance = InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dataset_rows_market_index_dataset_response_dict = insights_api_models_responses_balancing_dataset_rows_market_index_dataset_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse from a dict
insights_api_models_responses_balancing_dataset_rows_market_index_dataset_response_form_dict = insights_api_models_responses_balancing_dataset_rows_market_index_dataset_response.from_dict(insights_api_models_responses_balancing_dataset_rows_market_index_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


