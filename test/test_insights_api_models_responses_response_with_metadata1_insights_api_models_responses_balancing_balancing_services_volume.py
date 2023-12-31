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

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_balancing_services_volume import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume  # noqa: E501

class TestInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume(unittest.TestCase):
    """InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume:
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume`
        """
        model = InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume(
                data = [
                    openapi_client.models.insights/api/models/responses/balancing/balancing_services_volume.Insights.Api.Models.Responses.Balancing.BalancingServicesVolume(
                        settlement_date = 'Mon Jul 25 02:00:00 CEST 2022', 
                        settlement_period = 3, 
                        bm_unit_applicable_balancing_services_volume = 123.45, 
                        national_grid_bm_unit = 'ABRBO-1', 
                        bm_unit = 'T_ABRBO-1', 
                        time = '2022-07-25T09:34Z', )
                    ],
                metadata = openapi_client.models.insights/api/models/metadata/api_response_source_metadata.Insights.Api.Models.Metadata.ApiResponseSourceMetadata(
                    datasets = ["DATASET"], )
            )
        else:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume(
        )
        """

    def testInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume(self):
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
