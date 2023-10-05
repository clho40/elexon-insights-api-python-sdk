# InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**time_from** | **datetime** |  | [optional] 
**level_from** | **int** |  | [optional] 
**time_to** | **datetime** |  | [optional] 
**level_to** | **int** |  | [optional] 
**pair_id** | **int** |  | [optional] 
**offer** | **float** |  | [optional] 
**bid** | **float** |  | [optional] 
**national_grid_bm_unit** | **str** |  | [optional] 
**bm_unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_dataset_rows_bid_offer_dataset_response import InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse from a JSON string
insights_api_models_responses_balancing_dataset_rows_bid_offer_dataset_response_instance = InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_dataset_rows_bid_offer_dataset_response_dict = insights_api_models_responses_balancing_dataset_rows_bid_offer_dataset_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse from a dict
insights_api_models_responses_balancing_dataset_rows_bid_offer_dataset_response_form_dict = insights_api_models_responses_balancing_dataset_rows_bid_offer_dataset_response.from_dict(insights_api_models_responses_balancing_dataset_rows_bid_offer_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


