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

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_balancing_dynamic_dataset_rows_stable_portage_limit_data import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData(
                data = [
                    openapi_client.models.insights/api/models/responses/balancing/dynamic/dataset_rows/stable_portage_limit_data.Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.StablePortageLimitData(
                        dataset = 'SEL', 
                        settlement_date = 'Fri Jul 01 02:00:00 CEST 2022', 
                        settlement_period = 3, 
                        time = '2022-07-01T13:34Z', 
                        level = 5, 
                        national_grid_bm_unit = 'ABRBO-1', 
                        bm_unit = 'T_ABRBO-1', )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
