# InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**data** | [**List[InsightsApiModelsResponsesTransparencyActualGenerationValue]**](InsightsApiModelsResponsesTransparencyActualGenerationValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_transparency_actual_generation_by_settlement_period import InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod from a JSON string
insights_api_models_responses_transparency_actual_generation_by_settlement_period_instance = InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod.to_json()

# convert the object into a dict
insights_api_models_responses_transparency_actual_generation_by_settlement_period_dict = insights_api_models_responses_transparency_actual_generation_by_settlement_period_instance.to_dict()
# create an instance of InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod from a dict
insights_api_models_responses_transparency_actual_generation_by_settlement_period_form_dict = insights_api_models_responses_transparency_actual_generation_by_settlement_period.from_dict(insights_api_models_responses_transparency_actual_generation_by_settlement_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


