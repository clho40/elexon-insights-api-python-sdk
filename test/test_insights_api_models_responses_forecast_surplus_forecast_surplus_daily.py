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

from openapi_client.models.insights_api_models_responses_forecast_surplus_forecast_surplus_daily import InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily  # noqa: E501

class TestInsightsApiModelsResponsesForecastSurplusForecastSurplusDaily(unittest.TestCase):
    """InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily:
        """Test InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily`
        """
        model = InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily(
                publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                surplus = 56,
                forecast_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily(
        )
        """

    def testInsightsApiModelsResponsesForecastSurplusForecastSurplusDaily(self):
        """Test InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
