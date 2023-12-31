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

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_indicated_forecast_dataset_rows_indicated_imbalance import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance(
                data = [
                    openapi_client.models.insights/api/models/responses/indicated_forecast/dataset_rows/indicated_imbalance.Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedImbalance(
                        dataset = '', 
                        imbalance = 56, 
                        publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        settlement_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        settlement_period = 56, 
                        boundary = '', )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
