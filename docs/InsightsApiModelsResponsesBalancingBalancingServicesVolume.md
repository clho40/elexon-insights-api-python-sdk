# InsightsApiModelsResponsesBalancingBalancingServicesVolume


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**bm_unit_applicable_balancing_services_volume** | **float** |  | [optional] 
**national_grid_bm_unit** | **str** |  | [optional] 
**bm_unit** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_balancing_services_volume import InsightsApiModelsResponsesBalancingBalancingServicesVolume

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingBalancingServicesVolume from a JSON string
insights_api_models_responses_balancing_balancing_services_volume_instance = InsightsApiModelsResponsesBalancingBalancingServicesVolume.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingBalancingServicesVolume.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_balancing_services_volume_dict = insights_api_models_responses_balancing_balancing_services_volume_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingBalancingServicesVolume from a dict
insights_api_models_responses_balancing_balancing_services_volume_form_dict = insights_api_models_responses_balancing_balancing_services_volume.from_dict(insights_api_models_responses_balancing_balancing_services_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


