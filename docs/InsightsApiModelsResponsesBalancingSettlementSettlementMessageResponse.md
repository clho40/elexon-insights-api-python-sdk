# InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**message_received_date_time** | **datetime** |  | [optional] 
**message_severity** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**message_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_settlement_settlement_message_response import InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse from a JSON string
insights_api_models_responses_balancing_settlement_settlement_message_response_instance = InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_settlement_settlement_message_response_dict = insights_api_models_responses_balancing_settlement_settlement_message_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse from a dict
insights_api_models_responses_balancing_settlement_settlement_message_response_form_dict = insights_api_models_responses_balancing_settlement_settlement_message_response.from_dict(insights_api_models_responses_balancing_settlement_settlement_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


