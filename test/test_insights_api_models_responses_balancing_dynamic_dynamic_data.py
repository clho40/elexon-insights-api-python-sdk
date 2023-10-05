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

from openapi_client.models.insights_api_models_responses_balancing_dynamic_dynamic_data import InsightsApiModelsResponsesBalancingDynamicDynamicData  # noqa: E501

class TestInsightsApiModelsResponsesBalancingDynamicDynamicData(unittest.TestCase):
    """InsightsApiModelsResponsesBalancingDynamicDynamicData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesBalancingDynamicDynamicData:
        """Test InsightsApiModelsResponsesBalancingDynamicDynamicData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesBalancingDynamicDynamicData`
        """
        model = InsightsApiModelsResponsesBalancingDynamicDynamicData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesBalancingDynamicDynamicData(
                dataset = 'SEL',
                bm_unit = 'T_ABRBO-1',
                national_grid_bm_unit = 'ABRBO-1',
                time = '2022-07-01T13:34Z',
                value = 5,
                settlement_date = 'Fri Jul 01 02:00:00 CEST 2022',
                settlement_period = 3
            )
        else:
            return InsightsApiModelsResponsesBalancingDynamicDynamicData(
        )
        """

    def testInsightsApiModelsResponsesBalancingDynamicDynamicData(self):
        """Test InsightsApiModelsResponsesBalancingDynamicDynamicData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()