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

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_demand_outturn_rolling_system_demand import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand  # noqa: E501

class TestInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand(unittest.TestCase):
    """InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand:
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand`
        """
        model = InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand(
                data = [
                    openapi_client.models.insights/api/models/responses/demand_outturn/rolling_system_demand.Insights.Api.Models.Responses.DemandOutturn.RollingSystemDemand(
                        record_type = '', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        demand = 56, )
                    ],
                metadata = openapi_client.models.insights/api/models/metadata/api_response_source_metadata.Insights.Api.Models.Metadata.ApiResponseSourceMetadata(
                    datasets = ["DATASET"], )
            )
        else:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand(
        )
        """

    def testInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand(self):
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
