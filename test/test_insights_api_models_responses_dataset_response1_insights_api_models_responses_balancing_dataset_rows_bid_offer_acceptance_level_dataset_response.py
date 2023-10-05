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

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_balancing_dataset_rows_bid_offer_acceptance_level_dataset_response import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse(
                data = [
                    openapi_client.models.insights/api/models/responses/balancing/dataset_rows/bid_offer_acceptance_level_dataset_response.Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferAcceptanceLevelDatasetResponse(
                        dataset = 'BOALF', 
                        settlement_date = 'Mon Jul 25 02:00:00 CEST 2022', 
                        settlement_period_from = 29, 
                        settlement_period_to = 32, 
                        time_from = '2022-06-25T13:34Z', 
                        time_to = '2022-06-25T13:37Z', 
                        level_from = 5, 
                        level_to = 46, 
                        acceptance_number = 1234567, 
                        acceptance_time = '2022-06-25T13:37Z', 
                        deemed_bo_flag = True, 
                        so_flag = True, 
                        amendment_flag = 'ORI', 
                        stor_flag = True, 
                        rr_flag = True, 
                        national_grid_bm_unit = 'ABRBO-1', 
                        bm_unit = 'T_ABRBO-1', )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()