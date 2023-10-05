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

from openapi_client.models.insights_api_models_responses_generation_aggregated_forecast import InsightsApiModelsResponsesGenerationAggregatedForecast  # noqa: E501

class TestInsightsApiModelsResponsesGenerationAggregatedForecast(unittest.TestCase):
    """InsightsApiModelsResponsesGenerationAggregatedForecast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesGenerationAggregatedForecast:
        """Test InsightsApiModelsResponsesGenerationAggregatedForecast
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesGenerationAggregatedForecast`
        """
        model = InsightsApiModelsResponsesGenerationAggregatedForecast()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesGenerationAggregatedForecast(
                forecast_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                data = [
                    openapi_client.models.insights/api/models/responses/generation/forecast_fuel_data.Insights.Api.Models.Responses.Generation.ForecastFuelData(
                        fuel_type = '', 
                        output_usable = 56, )
                    ]
            )
        else:
            return InsightsApiModelsResponsesGenerationAggregatedForecast(
        )
        """

    def testInsightsApiModelsResponsesGenerationAggregatedForecast(self):
        """Test InsightsApiModelsResponsesGenerationAggregatedForecast"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
