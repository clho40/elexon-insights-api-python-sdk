# InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**volume_max** | **int** |  | [optional] 
**national_grid_bm_unit** | **str** |  | [optional] 
**bm_unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data import InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData from a JSON string
insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data_instance = InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data_dict = insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData from a dict
insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data_form_dict = insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data.from_dict(insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


