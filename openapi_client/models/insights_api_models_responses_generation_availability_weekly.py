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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class InsightsApiModelsResponsesGenerationAvailabilityWeekly(BaseModel):
    """
    InsightsApiModelsResponsesGenerationAvailabilityWeekly
    """
    dataset: Optional[StrictStr] = None
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    fuel_type: Optional[StrictStr] = Field(None, alias="fuelType")
    ngc_bm_unit: Optional[StrictStr] = Field(None, alias="ngcBmUnit")
    output_usable: Optional[StrictInt] = Field(None, alias="outputUsable")
    year: Optional[StrictInt] = None
    calendar_week_number: Optional[StrictInt] = Field(None, alias="calendarWeekNumber")
    __properties = ["dataset", "publishTime", "fuelType", "ngcBmUnit", "outputUsable", "year", "calendarWeekNumber"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesGenerationAvailabilityWeekly:
        """Create an instance of InsightsApiModelsResponsesGenerationAvailabilityWeekly from a JSON string"""
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

        # set to None if publish_time (nullable) is None
        # and __fields_set__ contains the field
        if self.publish_time is None and "publish_time" in self.__fields_set__:
            _dict['publishTime'] = None

        # set to None if fuel_type (nullable) is None
        # and __fields_set__ contains the field
        if self.fuel_type is None and "fuel_type" in self.__fields_set__:
            _dict['fuelType'] = None

        # set to None if ngc_bm_unit (nullable) is None
        # and __fields_set__ contains the field
        if self.ngc_bm_unit is None and "ngc_bm_unit" in self.__fields_set__:
            _dict['ngcBmUnit'] = None

        # set to None if output_usable (nullable) is None
        # and __fields_set__ contains the field
        if self.output_usable is None and "output_usable" in self.__fields_set__:
            _dict['outputUsable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesGenerationAvailabilityWeekly:
        """Create an instance of InsightsApiModelsResponsesGenerationAvailabilityWeekly from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesGenerationAvailabilityWeekly.parse_obj(obj)

        _obj = InsightsApiModelsResponsesGenerationAvailabilityWeekly.parse_obj({
            "dataset": obj.get("dataset"),
            "publish_time": obj.get("publishTime"),
            "fuel_type": obj.get("fuelType"),
            "ngc_bm_unit": obj.get("ngcBmUnit"),
            "output_usable": obj.get("outputUsable"),
            "year": obj.get("year"),
            "calendar_week_number": obj.get("calendarWeekNumber")
        })
        return _obj


