# InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period_from** | **int** |  | [optional] 
**settlement_period_to** | **int** |  | [optional] 
**time_from** | **datetime** |  | [optional] 
**time_to** | **datetime** |  | [optional] 
**level_from** | **int** |  | [optional] 
**level_to** | **int** |  | [optional] 
**acceptance_number** | **int** |  | [optional] 
**acceptance_time** | **datetime** |  | [optional] 
**deemed_bo_flag** | **bool** |  | [optional] 
**so_flag** | **bool** |  | [optional] 
**amendment_flag** | **str** |  | [optional] 
**stor_flag** | **bool** |  | [optional] 
**rr_flag** | **bool** |  | [optional] 
**national_grid_bm_unit** | **str** |  | [optional] 
**bm_unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response import InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse from a JSON string
insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response_instance = InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response_dict = insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse from a dict
insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response_form_dict = insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response.from_dict(insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


