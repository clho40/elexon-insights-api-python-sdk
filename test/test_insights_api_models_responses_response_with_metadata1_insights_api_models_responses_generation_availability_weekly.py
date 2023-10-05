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

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_generation_availability_weekly import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly  # noqa: E501

class TestInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly(unittest.TestCase):
    """InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly:
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly`
        """
        model = InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly(
                data = [
                    openapi_client.models.insights/api/models/responses/generation/availability_weekly.Insights.Api.Models.Responses.Generation.AvailabilityWeekly(
                        dataset = '', 
                        publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        fuel_type = '', 
                        ngc_bm_unit = '', 
                        output_usable = 56, 
                        year = 56, 
                        calendar_week_number = 56, )
                    ],
                metadata = openapi_client.models.insights/api/models/metadata/api_response_source_metadata.Insights.Api.Models.Metadata.ApiResponseSourceMetadata(
                    datasets = ["DATASET"], )
            )
        else:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly(
        )
        """

    def testInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly(self):
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()