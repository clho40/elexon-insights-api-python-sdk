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

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_misc_dataset_rows_system_frequency import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency(
                data = [
                    openapi_client.models.insights/api/models/responses/misc/dataset_rows/system_frequency.Insights.Api.Models.Responses.Misc.DatasetRows.SystemFrequency(
                        dataset = '', 
                        measurement_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        frequency = 1.337, )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
