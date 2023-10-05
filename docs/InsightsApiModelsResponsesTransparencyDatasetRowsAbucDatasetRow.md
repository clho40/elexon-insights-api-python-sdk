# InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**document_revision_number** | **int** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**business_type** | **str** |  | [optional] 
**psr_type** | **str** |  | [optional] 
**market_agreement_type** | **str** |  | [optional] 
**flow_direction** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_transparency_dataset_rows_abuc_dataset_row import InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow from a JSON string
insights_api_models_responses_transparency_dataset_rows_abuc_dataset_row_instance = InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.to_json()

# convert the object into a dict
insights_api_models_responses_transparency_dataset_rows_abuc_dataset_row_dict = insights_api_models_responses_transparency_dataset_rows_abuc_dataset_row_instance.to_dict()
# create an instance of InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow from a dict
insights_api_models_responses_transparency_dataset_rows_abuc_dataset_row_form_dict = insights_api_models_responses_transparency_dataset_rows_abuc_dataset_row.from_dict(insights_api_models_responses_transparency_dataset_rows_abuc_dataset_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


