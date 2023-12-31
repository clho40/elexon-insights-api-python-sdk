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

from openapi_client.models.insights_api_models_responses_misc_demand_control_instruction_data import InsightsApiModelsResponsesMiscDemandControlInstructionData  # noqa: E501

class TestInsightsApiModelsResponsesMiscDemandControlInstructionData(unittest.TestCase):
    """InsightsApiModelsResponsesMiscDemandControlInstructionData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesMiscDemandControlInstructionData:
        """Test InsightsApiModelsResponsesMiscDemandControlInstructionData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesMiscDemandControlInstructionData`
        """
        model = InsightsApiModelsResponsesMiscDemandControlInstructionData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesMiscDemandControlInstructionData(
                m_rid = 'DCI_202104300853_00000030',
                revision_number = 1,
                publish_time = '2021-04-30T08:53:39Z',
                publishing_period_commencing_time = '2021-04-30T08:53:39Z',
                affected_dso = 'SP(D)',
                demand_control_id = '00135',
                instruction_sequence = 1,
                demand_control_event_flag = 'I',
                time_from = '2021-04-30T12:45Z',
                time_to = '2021-04-30T13:09Z',
                volume = 68,
                system_management_action_flag = 'T',
                amendment_flag = 'ORI'
            )
        else:
            return InsightsApiModelsResponsesMiscDemandControlInstructionData(
        )
        """

    def testInsightsApiModelsResponsesMiscDemandControlInstructionData(self):
        """Test InsightsApiModelsResponsesMiscDemandControlInstructionData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
