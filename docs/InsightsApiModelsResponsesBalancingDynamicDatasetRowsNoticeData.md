# InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**notice** | **int** |  | [optional] 
**national_grid_bm_unit** | **str** |  | [optional] 
**bm_unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dynamic_dataset_rows_notice_data import InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData from a JSON string
insights_api_models_responses_balancing_dynamic_dataset_rows_notice_data_instance = InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dynamic_dataset_rows_notice_data_dict = insights_api_models_responses_balancing_dynamic_dataset_rows_notice_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData from a dict
insights_api_models_responses_balancing_dynamic_dataset_rows_notice_data_form_dict = insights_api_models_responses_balancing_dynamic_dataset_rows_notice_data.from_dict(insights_api_models_responses_balancing_dynamic_dataset_rows_notice_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


