# InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**m_rid** | **str** |  | [optional] 
**revision_number** | **int** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**publishing_period_commencing_time** | **datetime** |  | [optional] 
**affected_dso** | **str** |  | [optional] 
**demand_control_id** | **str** |  | [optional] 
**instruction_sequence** | **int** |  | [optional] 
**demand_control_event_flag** | **str** |  | [optional] 
**time_from** | **datetime** |  | [optional] 
**time_to** | **datetime** |  | [optional] 
**volume** | **float** |  | [optional] 
**system_management_action_flag** | **str** |  | [optional] 
**amendment_flag** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_misc_dataset_rows_demand_control_instruction_dataset_row import InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow from a JSON string
insights_api_models_responses_misc_dataset_rows_demand_control_instruction_dataset_row_instance = InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow.to_json()

# convert the object into a dict
insights_api_models_responses_misc_dataset_rows_demand_control_instruction_dataset_row_dict = insights_api_models_responses_misc_dataset_rows_demand_control_instruction_dataset_row_instance.to_dict()
# create an instance of InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow from a dict
insights_api_models_responses_misc_dataset_rows_demand_control_instruction_dataset_row_form_dict = insights_api_models_responses_misc_dataset_rows_demand_control_instruction_dataset_row.from_dict(insights_api_models_responses_misc_dataset_rows_demand_control_instruction_dataset_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


