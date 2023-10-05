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

from openapi_client.models.insights_api_models_responses_transparency_dataset_rows_year_ahead_forecast_margin_dataset_row import InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow  # noqa: E501

class TestInsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow(unittest.TestCase):
    """InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow:
        """Test InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow`
        """
        model = InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow(
                dataset = 'YAFM',
                document_id = 'NGET-EMFIP-YAFM-00687705',
                document_revision_number = 1,
                publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                business_type = 'Positive forecast margin',
                year = 2023,
                quantity = 1.08
            )
        else:
            return InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow(
        )
        """

    def testInsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow(self):
        """Test InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
