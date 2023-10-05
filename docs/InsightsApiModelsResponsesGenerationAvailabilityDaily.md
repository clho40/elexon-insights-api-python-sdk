# InsightsApiModelsResponsesGenerationAvailabilityDaily


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**fuel_type** | **str** |  | [optional] 
**ngc_bm_unit** | **str** |  | [optional] 
**output_usable** | **int** |  | [optional] 
**forecast_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_generation_availability_daily import InsightsApiModelsResponsesGenerationAvailabilityDaily

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesGenerationAvailabilityDaily from a JSON string
insights_api_models_responses_generation_availability_daily_instance = InsightsApiModelsResponsesGenerationAvailabilityDaily.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesGenerationAvailabilityDaily.to_json()

# convert the object into a dict
insights_api_models_responses_generation_availability_daily_dict = insights_api_models_responses_generation_availability_daily_instance.to_dict()
# create an instance of InsightsApiModelsResponsesGenerationAvailabilityDaily from a dict
insights_api_models_responses_generation_availability_daily_form_dict = insights_api_models_responses_generation_availability_daily.from_dict(insights_api_models_responses_generation_availability_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


