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

from openapi_client.models.insights_api_models_responses_generation_half_hourly_interconnector_outturn import InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn  # noqa: E501

class TestInsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn(unittest.TestCase):
    """InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn:
        """Test InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn`
        """
        model = InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn(
                dataset = '',
                publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                settlement_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                settlement_date_timezone = '',
                settlement_period = 56,
                interconnector_name = '',
                generation = 56
            )
        else:
            return InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn(
        )
        """

    def testInsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn(self):
        """Test InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
