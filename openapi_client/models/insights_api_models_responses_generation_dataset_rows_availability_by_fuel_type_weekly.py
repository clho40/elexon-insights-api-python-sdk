# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly(BaseModel):
    """
    InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly
    """
    dataset: Optional[StrictStr] = None
    fuel_type: Optional[StrictStr] = Field(None, alias="fuelType")
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    system_zone: Optional[StrictStr] = Field(None, alias="systemZone")
    calendar_week_number: Optional[StrictInt] = Field(None, alias="calendarWeekNumber")
    year: Optional[StrictInt] = None
    output_usable: Optional[StrictInt] = Field(None, alias="outputUsable")
    bidding_zone: Optional[StrictStr] = Field(None, alias="biddingZone")
    interconnector_name: Optional[StrictStr] = Field(None, alias="interconnectorName")
    interconnector: Optional[StrictBool] = None
    __properties = ["dataset", "fuelType", "publishTime", "systemZone", "calendarWeekNumber", "year", "outputUsable", "biddingZone", "interconnectorName", "interconnector"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly:
        """Create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if dataset (nullable) is None
        # and __fields_set__ contains the field
        if self.dataset is None and "dataset" in self.__fields_set__:
            _dict['dataset'] = None

        # set to None if fuel_type (nullable) is None
        # and __fields_set__ contains the field
        if self.fuel_type is None and "fuel_type" in self.__fields_set__:
            _dict['fuelType'] = None

        # set to None if publish_time (nullable) is None
        # and __fields_set__ contains the field
        if self.publish_time is None and "publish_time" in self.__fields_set__:
            _dict['publishTime'] = None

        # set to None if system_zone (nullable) is None
        # and __fields_set__ contains the field
        if self.system_zone is None and "system_zone" in self.__fields_set__:
            _dict['systemZone'] = None

        # set to None if calendar_week_number (nullable) is None
        # and __fields_set__ contains the field
        if self.calendar_week_number is None and "calendar_week_number" in self.__fields_set__:
            _dict['calendarWeekNumber'] = None

        # set to None if year (nullable) is None
        # and __fields_set__ contains the field
        if self.year is None and "year" in self.__fields_set__:
            _dict['year'] = None

        # set to None if output_usable (nullable) is None
        # and __fields_set__ contains the field
        if self.output_usable is None and "output_usable" in self.__fields_set__:
            _dict['outputUsable'] = None

        # set to None if bidding_zone (nullable) is None
        # and __fields_set__ contains the field
        if self.bidding_zone is None and "bidding_zone" in self.__fields_set__:
            _dict['biddingZone'] = None

        # set to None if interconnector_name (nullable) is None
        # and __fields_set__ contains the field
        if self.interconnector_name is None and "interconnector_name" in self.__fields_set__:
            _dict['interconnectorName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly:
        """Create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly.parse_obj(obj)

        _obj = InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly.parse_obj({
            "dataset": obj.get("dataset"),
            "fuel_type": obj.get("fuelType"),
            "publish_time": obj.get("publishTime"),
            "system_zone": obj.get("systemZone"),
            "calendar_week_number": obj.get("calendarWeekNumber"),
            "year": obj.get("year"),
            "output_usable": obj.get("outputUsable"),
            "bidding_zone": obj.get("biddingZone"),
            "interconnector_name": obj.get("interconnectorName"),
            "interconnector": obj.get("interconnector")
        })
        return _obj


