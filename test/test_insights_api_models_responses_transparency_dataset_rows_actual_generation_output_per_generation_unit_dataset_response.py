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

from openapi_client.models.insights_api_models_responses_transparency_dataset_rows_actual_generation_output_per_generation_unit_dataset_response import InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse  # noqa: E501

class TestInsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse(unittest.TestCase):
    """InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse:
        """Test InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse`
        """
        model = InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse(
                dataset = 'B1610',
                psr_type = 'Generation',
                bm_unit = 'T_CNQPS-1',
                national_grid_bm_unit_id = 'CNQPS-1',
                settlement_date = 'Fri Aug 12 02:00:00 CEST 2022',
                settlement_period = 10,
                half_hour_end_time = '2022-08-12T04:00Z',
                quantity = 116.109
            )
        else:
            return InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse(
        )
        """

    def testInsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse(self):
        """Test InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()