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

from openapi_client.models.insights_api_models_responses_demand_outturn_indicative_demand_peak import InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak  # noqa: E501

class TestInsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak(unittest.TestCase):
    """InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak:
        """Test InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak`
        """
        model = InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak(
                settlement_date = 'Fri Oct 01 02:00:00 CEST 2021',
                settlement_period = 3,
                half_hour_end_time = '2021-10-01T01:00Z',
                demand = 36256,
                settlement_run_type = 'II'
            )
        else:
            return InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak(
        )
        """

    def testInsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak(self):
        """Test InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
