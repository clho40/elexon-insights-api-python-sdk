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

from openapi_client.models.insights_api_models_responses_demand_forecast_demand_forecast_weekly import InsightsApiModelsResponsesDemandForecastDemandForecastWeekly  # noqa: E501

class TestInsightsApiModelsResponsesDemandForecastDemandForecastWeekly(unittest.TestCase):
    """InsightsApiModelsResponsesDemandForecastDemandForecastWeekly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDemandForecastDemandForecastWeekly:
        """Test InsightsApiModelsResponsesDemandForecastDemandForecastWeekly
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDemandForecastDemandForecastWeekly`
        """
        model = InsightsApiModelsResponsesDemandForecastDemandForecastWeekly()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDemandForecastDemandForecastWeekly(
                publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                transmission_system_demand = 56,
                national_demand = 56,
                forecast_week = 56,
                forecast_year = 56,
                week_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return InsightsApiModelsResponsesDemandForecastDemandForecastWeekly(
        )
        """

    def testInsightsApiModelsResponsesDemandForecastDemandForecastWeekly(self):
        """Test InsightsApiModelsResponsesDemandForecastDemandForecastWeekly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
