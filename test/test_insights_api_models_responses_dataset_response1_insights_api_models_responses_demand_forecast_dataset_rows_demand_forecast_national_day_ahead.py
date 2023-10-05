# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_demand_forecast_dataset_rows_demand_forecast_national_day_ahead import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead(
                data = [
                    openapi_client.models.insights/api/models/responses/demand_forecast/dataset_rows/demand_forecast_national_day_ahead.Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDayAhead(
                        dataset = '', 
                        demand = 56, 
                        publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        settlement_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        settlement_period = 56, 
                        boundary = '', )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
