# InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**settlement_period** | **int** |  | [optional] 
**initial_transmission_system_demand_outturn** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.insights_api_models_responses_demand_outturn_demand_outturn_peak import InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak from a JSON string
insights_api_models_responses_demand_outturn_demand_outturn_peak_instance = InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.from_json(json)
# print the JSON string representation of the object
print InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.to_json()

# convert the object into a dict
insights_api_models_responses_demand_outturn_demand_outturn_peak_dict = insights_api_models_responses_demand_outturn_demand_outturn_peak_instance.to_dict()
# create an instance of InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak from a dict
insights_api_models_responses_demand_outturn_demand_outturn_peak_form_dict = insights_api_models_responses_demand_outturn_demand_outturn_peak.from_dict(insights_api_models_responses_demand_outturn_demand_outturn_peak_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


