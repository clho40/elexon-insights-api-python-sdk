# InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**bsc_party_id** | **str** |  | [optional] 
**credit_default_level** | **int** |  | [optional] 
**entered_default_settlement_date** | **date** |  | [optional] 
**entered_default_settlement_period** | **int** |  | [optional] 
**cleared_default_settlement_date** | **date** |  | [optional] 
**cleared_default_settlement_period** | **int** |  | [optional] 
**cleared_default_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dataset_rows_credit_default_notice_dataset_response import InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse from a JSON string
insights_api_models_responses_balancing_dataset_rows_credit_default_notice_dataset_response_instance = InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dataset_rows_credit_default_notice_dataset_response_dict = insights_api_models_responses_balancing_dataset_rows_credit_default_notice_dataset_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse from a dict
insights_api_models_responses_balancing_dataset_rows_credit_default_notice_dataset_response_form_dict = insights_api_models_responses_balancing_dataset_rows_credit_default_notice_dataset_response.from_dict(insights_api_models_responses_balancing_dataset_rows_credit_default_notice_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


