# InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**buy_action_count** | **int** |  | [optional] 
**sell_action_count** | **int** |  | [optional] 
**buy_price_minimum** | **float** |  | [optional] 
**buy_price_maximum** | **float** |  | [optional] 
**buy_price_average** | **float** |  | [optional] 
**sell_price_minimum** | **float** |  | [optional] 
**sell_price_maximum** | **float** |  | [optional] 
**sell_price_average** | **float** |  | [optional] 
**buy_volume_total** | **float** |  | [optional] 
**sell_volume_total** | **float** |  | [optional] 
**net_volume** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response import InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse from a JSON string
insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response_instance = InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response_dict = insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse from a dict
insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response_form_dict = insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response.from_dict(insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


