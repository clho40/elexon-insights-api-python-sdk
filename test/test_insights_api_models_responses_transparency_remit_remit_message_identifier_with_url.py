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

from openapi_client.models.insights_api_models_responses_transparency_remit_remit_message_identifier_with_url import InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl  # noqa: E501

class TestInsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl(unittest.TestCase):
    """InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl:
        """Test InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl`
        """
        model = InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl(
                id = 24,
                mrid = '11XINNOGY------2-NGET-RMT-00084421',
                revision_number = 2,
                created_time = '2023-01-31T17:39:15Z',
                url = 'https://data.elexon.co.uk/bmrs/api/v1/remit/24'
            )
        else:
            return InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl(
        )
        """

    def testInsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl(self):
        """Test InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
