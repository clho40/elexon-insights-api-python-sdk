# InsightsApiModelsResponsesBalancingDynamicDynamicData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**bm_unit** | **str** |  | [optional] 
**national_grid_bm_unit** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**value** | **int** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dynamic_dynamic_data import InsightsApiModelsResponsesBalancingDynamicDynamicData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDynamicDynamicData from a JSON string
insights_api_models_responses_balancing_dynamic_dynamic_data_instance = InsightsApiModelsResponsesBalancingDynamicDynamicData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDynamicDynamicData.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dynamic_dynamic_data_dict = insights_api_models_responses_balancing_dynamic_dynamic_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDynamicDynamicData from a dict
insights_api_models_responses_balancing_dynamic_dynamic_data_form_dict = insights_api_models_responses_balancing_dynamic_dynamic_data.from_dict(insights_api_models_responses_balancing_dynamic_dynamic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


