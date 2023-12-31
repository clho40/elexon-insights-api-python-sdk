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

from openapi_client.models.insights_api_models_responses_demand_outturn_indod_row import InsightsApiModelsResponsesDemandOutturnIndodRow  # noqa: E501

class TestInsightsApiModelsResponsesDemandOutturnIndodRow(unittest.TestCase):
    """InsightsApiModelsResponsesDemandOutturnIndodRow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDemandOutturnIndodRow:
        """Test InsightsApiModelsResponsesDemandOutturnIndodRow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDemandOutturnIndodRow`
        """
        model = InsightsApiModelsResponsesDemandOutturnIndodRow()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDemandOutturnIndodRow(
                publish_time = '2023-08-26T23:15Z',
                settlement_date = 'Sat Aug 26 02:00:00 CEST 2023',
                demand = 494802
            )
        else:
            return InsightsApiModelsResponsesDemandOutturnIndodRow(
        )
        """

    def testInsightsApiModelsResponsesDemandOutturnIndodRow(self):
        """Test InsightsApiModelsResponsesDemandOutturnIndodRow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
