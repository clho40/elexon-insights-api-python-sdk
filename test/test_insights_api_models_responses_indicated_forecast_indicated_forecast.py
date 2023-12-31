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

from openapi_client.models.insights_api_models_responses_indicated_forecast_indicated_forecast import InsightsApiModelsResponsesIndicatedForecastIndicatedForecast  # noqa: E501

class TestInsightsApiModelsResponsesIndicatedForecastIndicatedForecast(unittest.TestCase):
    """InsightsApiModelsResponsesIndicatedForecastIndicatedForecast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesIndicatedForecastIndicatedForecast:
        """Test InsightsApiModelsResponsesIndicatedForecastIndicatedForecast
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesIndicatedForecastIndicatedForecast`
        """
        model = InsightsApiModelsResponsesIndicatedForecastIndicatedForecast()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesIndicatedForecastIndicatedForecast(
                publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                settlement_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                settlement_period = 56,
                boundary = '',
                indicated_generation = 56,
                indicated_demand = 56,
                indicated_margin = 56,
                indicated_imbalance = 56
            )
        else:
            return InsightsApiModelsResponsesIndicatedForecastIndicatedForecast(
        )
        """

    def testInsightsApiModelsResponsesIndicatedForecastIndicatedForecast(self):
        """Test InsightsApiModelsResponsesIndicatedForecastIndicatedForecast"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
