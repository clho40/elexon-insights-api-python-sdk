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

from openapi_client.models.insights_api_models_responses_generation_dataset_rows_augmented_outturn_data import InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData  # noqa: E501

class TestInsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData(unittest.TestCase):
    """InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData:
        """Test InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData`
        """
        model = InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData(
                dataset = 'FUELINST',
                publish_time = '2022-06-25T13:00Z',
                start_time = '2022-06-25T13:00Z',
                settlement_date = 'Sat Jun 25 02:00:00 CEST 2022',
                settlement_period = 3,
                fuel_type = 'BIOMASS',
                generation = 0
            )
        else:
            return InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData(
        )
        """

    def testInsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData(self):
        """Test InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
