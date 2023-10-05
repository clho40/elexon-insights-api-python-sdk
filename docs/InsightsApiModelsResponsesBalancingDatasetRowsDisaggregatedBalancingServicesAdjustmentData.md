# InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**cost** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 
**so_flag** | **bool** |  | [optional] 
**stor_flag** | **bool** |  | [optional] 
**party_id** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**is_tendered** | **bool** |  | [optional] 
**service** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dataset_rows_disaggregated_balancing_services_adjustment_data import InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData from a JSON string
insights_api_models_responses_balancing_dataset_rows_disaggregated_balancing_services_adjustment_data_instance = InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dataset_rows_disaggregated_balancing_services_adjustment_data_dict = insights_api_models_responses_balancing_dataset_rows_disaggregated_balancing_services_adjustment_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData from a dict
insights_api_models_responses_balancing_dataset_rows_disaggregated_balancing_services_adjustment_data_form_dict = insights_api_models_responses_balancing_dataset_rows_disaggregated_balancing_services_adjustment_data.from_dict(insights_api_models_responses_balancing_dataset_rows_disaggregated_balancing_services_adjustment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


