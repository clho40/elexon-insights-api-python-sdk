# InsightsApiModelsResponsesReferenceBmUnitData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**national_grid_bm_unit** | **str** |  | [optional] 
**elexon_bm_unit** | **str** |  | [optional] 
**fuel_type** | **str** |  | [optional] 
**lead_party_name** | **str** |  | [optional] 
**bm_unit_type** | **str** |  | [optional] 
**fpn_flag** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_reference_bm_unit_data import InsightsApiModelsResponsesReferenceBmUnitData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesReferenceBmUnitData from a JSON string
insights_api_models_responses_reference_bm_unit_data_instance = InsightsApiModelsResponsesReferenceBmUnitData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesReferenceBmUnitData.to_json()

# convert the object into a dict
insights_api_models_responses_reference_bm_unit_data_dict = insights_api_models_responses_reference_bm_unit_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesReferenceBmUnitData from a dict
insights_api_models_responses_reference_bm_unit_data_form_dict = insights_api_models_responses_reference_bm_unit_data.from_dict(insights_api_models_responses_reference_bm_unit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


