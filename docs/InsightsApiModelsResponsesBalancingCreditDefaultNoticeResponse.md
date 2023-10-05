# InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant_id** | **str** |  | [optional] 
**participant_name** | **str** |  | [optional] 
**credit_default_level** | **int** |  | [optional] 
**entered_default_settlement_date** | **date** |  | [optional] 
**entered_default_settlement_period** | **int** |  | [optional] 
**cleared_default_settlement_date** | **date** |  | [optional] 
**cleared_default_settlement_period** | **int** |  | [optional] 
**cleared_default_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_credit_default_notice_response import InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse from a JSON string
insights_api_models_responses_balancing_credit_default_notice_response_instance = InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_credit_default_notice_response_dict = insights_api_models_responses_balancing_credit_default_notice_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse from a dict
insights_api_models_responses_balancing_credit_default_notice_response_form_dict = insights_api_models_responses_balancing_credit_default_notice_response.from_dict(insights_api_models_responses_balancing_credit_default_notice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


