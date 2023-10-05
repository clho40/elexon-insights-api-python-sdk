# InsightsApiModelsResponsesTransparencyAgptSummaryData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psr_type** | **str** |  | [optional] 
**half_hour_usage** | **float** |  | [optional] 
**half_hour_percentage** | **float** |  | [optional] 
**twenty_four_hour_usage** | **float** |  | [optional] 
**twenty_four_hour_percentage** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_transparency_agpt_summary_data import InsightsApiModelsResponsesTransparencyAgptSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesTransparencyAgptSummaryData from a JSON string
insights_api_models_responses_transparency_agpt_summary_data_instance = InsightsApiModelsResponsesTransparencyAgptSummaryData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesTransparencyAgptSummaryData.to_json()

# convert the object into a dict
insights_api_models_responses_transparency_agpt_summary_data_dict = insights_api_models_responses_transparency_agpt_summary_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesTransparencyAgptSummaryData from a dict
insights_api_models_responses_transparency_agpt_summary_data_form_dict = insights_api_models_responses_transparency_agpt_summary_data.from_dict(insights_api_models_responses_transparency_agpt_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


