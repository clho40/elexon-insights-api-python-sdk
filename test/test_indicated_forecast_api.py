# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.indicated_forecast_api import IndicatedForecastApi  # noqa: E501


class TestIndicatedForecastApi(unittest.TestCase):
    """IndicatedForecastApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IndicatedForecastApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_forecast_indicated_day_ahead_evolution_get(self) -> None:
        """Test case for forecast_indicated_day_ahead_evolution_get

        Evolution Indicated day-ahead forecast  # noqa: E501
        """
        pass

    def test_forecast_indicated_day_ahead_get(self) -> None:
        """Test case for forecast_indicated_day_ahead_get

        Latest indicated day-ahead forecast  # noqa: E501
        """
        pass

    def test_forecast_indicated_day_ahead_history_get(self) -> None:
        """Test case for forecast_indicated_day_ahead_history_get

        Historical indicated day-ahead forecast  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
