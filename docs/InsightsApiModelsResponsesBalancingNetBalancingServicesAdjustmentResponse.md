# InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**net_buy_price_cost_adjustment_energy** | **float** |  | [optional] 
**net_buy_price_volume_adjustment_energy** | **float** |  | [optional] 
**net_buy_price_volume_adjustment_system** | **float** |  | [optional] 
**buy_price_price_adjustment** | **float** |  | [optional] 
**net_sell_price_cost_adjustment_energy** | **float** |  | [optional] 
**net_sell_price_volume_adjustment_energy** | **float** |  | [optional] 
**net_sell_price_volume_adjustment_system** | **float** |  | [optional] 
**sell_price_price_adjustment** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_balancing_net_balancing_services_adjustment_response import InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse from a JSON string
insights_api_models_responses_balancing_net_balancing_services_adjustment_response_instance = InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse.to_json()

# convert the object into a dict
insights_api_models_responses_balancing_net_balancing_services_adjustment_response_dict = insights_api_models_responses_balancing_net_balancing_services_adjustment_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse from a dict
insights_api_models_responses_balancing_net_balancing_services_adjustment_response_form_dict = insights_api_models_responses_balancing_net_balancing_services_adjustment_response.from_dict(insights_api_models_responses_balancing_net_balancing_services_adjustment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


