# InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**cost** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**so_flag** | **bool** |  | [optional] 
**stor_flag** | **bool** |  | [optional] 
**party_id** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**is_tendered** | **bool** |  | [optional] 
**service** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response import InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse from a JSON string
insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response_instance = InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response_dict = insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse from a dict
insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response_form_dict = insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response.from_dict(insights_api_models_responses_balancing_disaggregated_balancing_services_adjustment_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


