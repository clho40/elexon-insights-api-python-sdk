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

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_dynamic_rate_data import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData  # noqa: E501

class TestInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData(unittest.TestCase):
    """InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData:
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData`
        """
        model = InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData(
                data = [
                    openapi_client.models.insights/api/models/responses/balancing/dynamic/rate_data.Insights.Api.Models.Responses.Balancing.Dynamic.RateData(
                        dataset = 'RURE', 
                        settlement_date = 'Fri Jul 01 02:00:00 CEST 2022', 
                        settlement_period = 3, 
                        time = '2022-07-01T13:34Z', 
                        rate1 = 0.4, 
                        elbow2 = 5, 
                        rate2 = 300.2, 
                        elbow3 = 1.337, 
                        rate3 = 1.337, 
                        national_grid_bm_unit = 'ABRBO-1', 
                        bm_unit = 'T_ABRBO-1', )
                    ],
                metadata = openapi_client.models.insights/api/models/metadata/api_response_source_metadata.Insights.Api.Models.Metadata.ApiResponseSourceMetadata(
                    datasets = ["DATASET"], )
            )
        else:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData(
        )
        """

    def testInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData(self):
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
