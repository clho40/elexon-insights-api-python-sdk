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

from openapi_client.models.insights_api_models_responses_transparency_dataset_rows_igca_dataset_row import InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow  # noqa: E501

class TestInsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow(unittest.TestCase):
    """InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow:
        """Test InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow`
        """
        model = InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow(
                dataset = 'IGCA',
                document_id = 'NGET-EMFIP-IGCA-00687002',
                document_revision_number = 1,
                publish_time = '2022-04-21T13:25:52Z',
                business_type = 'Installed generation',
                psr_type = 'Hydro Pumped Storage',
                year = 2022,
                quantity = 1928
            )
        else:
            return InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow(
        )
        """

    def testInsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow(self):
        """Test InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
