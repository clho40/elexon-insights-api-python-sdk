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

from openapi_client.models.insights_api_models_responses_demand_forecast_dataset_rows_demand_forecast_transmission_daily import InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily  # noqa: E501

class TestInsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily(unittest.TestCase):
    """InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily:
        """Test InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily`
        """
        model = InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily(
                dataset = '',
                publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                forecast_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                demand = 56
            )
        else:
            return InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily(
        )
        """

    def testInsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily(self):
        """Test InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()