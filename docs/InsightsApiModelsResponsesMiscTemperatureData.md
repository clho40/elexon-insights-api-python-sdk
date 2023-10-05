# InsightsApiModelsResponsesMiscTemperatureData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measurement_date** | **date** |  | [optional] 
**publish_time** | **datetime** |  | [optional] 
**temperature** | **float** |  | [optional] 
**temperature_reference_average** | **float** |  | [optional] 
**temperature_reference_high** | **float** |  | [optional] 
**temperature_reference_low** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_misc_temperature_data import InsightsApiModelsResponsesMiscTemperatureData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesMiscTemperatureData from a JSON string
insights_api_models_responses_misc_temperature_data_instance = InsightsApiModelsResponsesMiscTemperatureData.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesMiscTemperatureData.to_json()

# convert the object into a dict
insights_api_models_responses_misc_temperature_data_dict = insights_api_models_responses_misc_temperature_data_instance.to_dict()
# create an instance of InsightsApiModelsResponsesMiscTemperatureData from a dict
insights_api_models_responses_misc_temperature_data_form_dict = insights_api_models_responses_misc_temperature_data.from_dict(insights_api_models_responses_misc_temperature_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


