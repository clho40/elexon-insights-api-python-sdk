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

from openapi_client.models.insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_period_min_data import InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData  # noqa: E501

class TestInsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData(unittest.TestCase):
    """InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData:
        """Test InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData`
        """
        model = InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData(
                dataset = 'MZT',
                settlement_date = 'Mon Jul 25 02:00:00 CEST 2022',
                settlement_period = 3,
                time = '2022-07-25T09:34Z',
                period_min = 360,
                national_grid_bm_unit = 'ABRBO-1',
                bm_unit = 'T_ABRBO-1'
            )
        else:
            return InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData(
        )
        """

    def testInsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData(self):
        """Test InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()