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

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_balancing_dynamic_dataset_rows_delivery_volume_max_data import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData(
                data = [
                    openapi_client.models.insights/api/models/responses/balancing/dynamic/dataset_rows/delivery_volume_max_data.Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryVolumeMaxData(
                        dataset = 'MDV', 
                        settlement_date = 'Fri Jul 01 02:00:00 CEST 2022', 
                        settlement_period = 3, 
                        time = '2022-07-01T13:34Z', 
                        volume_max = 31, 
                        national_grid_bm_unit = 'ABRBO-1', 
                        bm_unit = 'T_ABRBO-1', )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
