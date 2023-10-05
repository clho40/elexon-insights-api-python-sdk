# InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**publishing_period_commencing_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**forecast_horizon** | **float** |  | [optional] 
**loss_of_load_probability** | **float** |  | [optional] 
**derated_margin** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response import InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse from a JSON string
insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response_instance = InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse.to_json()

# convert the object into a dict
insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response_dict = insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response_instance.to_dict()
# create an instance of InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse from a dict
insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response_form_dict = insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response.from_dict(insights_api_models_responses_misc_loss_of_load_probability_derated_margin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


