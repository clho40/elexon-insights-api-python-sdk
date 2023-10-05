# InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**net_buy_price_cost_adjustment_energy** | **float** |  | [optional] 
**net_buy_price_volume_adjustment_energy** | **float** |  | [optional] 
**net_buy_price_volume_adjustment_system** | **float** |  | [optional] 
**buy_price_price_adjustment** | **float** |  | [optional] 
**net_sell_price_cost_adjustment_energy** | **float** |  | [optional] 
**net_sell_price_volume_adjustment_energy** | **float** |  | [optional] 
**net_sell_price_volume_adjustment_system** | **float** |  | [optional] 
**sell_price_price_adjustment** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dataset_rows_net_balancing_services_adjustment_data import InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData from a JSON string
insights_api_models_responses_balancing_dataset_rows_net_balancing_services_adjustment_data_instance = InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dataset_rows_net_balancing_services_adjustment_data_dict = insights_api_models_responses_balancing_dataset_rows_net_balancing_services_adjustment_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData from a dict
insights_api_models_responses_balancing_dataset_rows_net_balancing_services_adjustment_data_form_dict = insights_api_models_responses_balancing_dataset_rows_net_balancing_services_adjustment_data.from_dict(insights_api_models_responses_balancing_dataset_rows_net_balancing_services_adjustment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


