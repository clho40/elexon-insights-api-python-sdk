# InsightsApiModelsResponsesBalancingNonBmStorResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**generation** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_non_bm_stor_response import InsightsApiModelsResponsesBalancingNonBmStorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingNonBmStorResponse from a JSON string
insights_api_models_responses_balancing_non_bm_stor_response_instance = InsightsApiModelsResponsesBalancingNonBmStorResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingNonBmStorResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_non_bm_stor_response_dict = insights_api_models_responses_balancing_non_bm_stor_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingNonBmStorResponse from a dict
insights_api_models_responses_balancing_non_bm_stor_response_form_dict = insights_api_models_responses_balancing_non_bm_stor_response.from_dict(insights_api_models_responses_balancing_non_bm_stor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


