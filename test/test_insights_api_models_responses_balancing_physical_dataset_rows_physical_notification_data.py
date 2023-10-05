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

from openapi_client.models.insights_api_models_responses_balancing_physical_dataset_rows_physical_notification_data import InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData  # noqa: E501

class TestInsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData(unittest.TestCase):
    """InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData:
        """Test InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData`
        """
        model = InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData(
                dataset = 'PN',
                settlement_date = 'Fri Jul 01 02:00:00 CEST 2022',
                settlement_period = 3,
                time_from = '2022-07-01T13:34Z',
                time_to = '2022-07-01T13:34Z',
                level_from = 5,
                level_to = 46,
                national_grid_bm_unit = 'ABRBO-1',
                bm_unit = 'T_ABRBO-1'
            )
        else:
            return InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData(
        )
        """

    def testInsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData(self):
        """Test InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
