# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.remit_api import RemitApi  # noqa: E501


class TestRemitApi(unittest.TestCase):
    """RemitApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RemitApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_r_emit_get(self) -> None:
        """Test case for r_emit_get

        Remit bulk data by Message IDs  # noqa: E501
        """
        pass

    def test_r_emit_list_by_event_get(self) -> None:
        """Test case for r_emit_list_by_event_get

        Remit list message identifiers by event  # noqa: E501
        """
        pass

    def test_r_emit_list_by_event_stream_get(self) -> None:
        """Test case for r_emit_list_by_event_stream_get

        Remit list message identifiers by event stream  # noqa: E501
        """
        pass

    def test_r_emit_list_by_publish_get(self) -> None:
        """Test case for r_emit_list_by_publish_get

        Remit list message identifiers by publish time  # noqa: E501
        """
        pass

    def test_r_emit_list_by_publish_stream_get(self) -> None:
        """Test case for r_emit_list_by_publish_stream_get

        Remit list message identifiers by publish time stream  # noqa: E501
        """
        pass

    def test_r_emit_message_id_get(self) -> None:
        """Test case for r_emit_message_id_get

        Remit data by Message ID  # noqa: E501
        """
        pass

    def test_r_emit_revisions_get(self) -> None:
        """Test case for r_emit_revisions_get

        Remit message revisions by MRID or Message ID  # noqa: E501
        """
        pass

    def test_r_emit_search_get(self) -> None:
        """Test case for r_emit_search_get

        Remit data by MRID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
