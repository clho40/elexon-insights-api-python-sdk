# InsightsApiModelsResponsesBalancingBidOfferResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**national_grid_bm_unit** | **str** |  | [optional] 
**bm_unit** | **str** |  | [optional] 
**time_from** | **datetime** |  | [optional] 
**time_to** | **datetime** |  | [optional] 
**level_from** | **int** |  | [optional] 
**level_to** | **int** |  | [optional] 
**bid** | **float** |  | [optional] 
**offer** | **float** |  | [optional] 
**pair_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_bid_offer_response import InsightsApiModelsResponsesBalancingBidOfferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingBidOfferResponse from a JSON string
insights_api_models_responses_balancing_bid_offer_response_instance = InsightsApiModelsResponsesBalancingBidOfferResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingBidOfferResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_bid_offer_response_dict = insights_api_models_responses_balancing_bid_offer_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingBidOfferResponse from a dict
insights_api_models_responses_balancing_bid_offer_response_form_dict = insights_api_models_responses_balancing_bid_offer_response.from_dict(insights_api_models_responses_balancing_bid_offer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


