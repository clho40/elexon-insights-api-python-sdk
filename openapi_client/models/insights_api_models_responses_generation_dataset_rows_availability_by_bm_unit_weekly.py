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

class InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly(BaseModel):
    """
    InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly
    """
    dataset: Optional[StrictStr] = None
    fuel_type: Optional[StrictStr] = Field(None, alias="fuelType")
    national_grid_bm_unit: Optional[StrictStr] = Field(None, alias="nationalGridBmUnit")
    bm_unit: Optional[StrictStr] = Field(None, alias="bmUnit")
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    week: Optional[StrictInt] = None
    year: Optional[StrictInt] = None
    output_usable: Optional[StrictInt] = Field(None, alias="outputUsable")
    __properties = ["dataset", "fuelType", "nationalGridBmUnit", "bmUnit", "publishTime", "week", "year", "outputUsable"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly:
        """Create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly from a JSON string"""
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

        # set to None if national_grid_bm_unit (nullable) is None
        # and __fields_set__ contains the field
        if self.national_grid_bm_unit is None and "national_grid_bm_unit" in self.__fields_set__:
            _dict['nationalGridBmUnit'] = None

        # set to None if bm_unit (nullable) is None
        # and __fields_set__ contains the field
        if self.bm_unit is None and "bm_unit" in self.__fields_set__:
            _dict['bmUnit'] = None

        # set to None if publish_time (nullable) is None
        # and __fields_set__ contains the field
        if self.publish_time is None and "publish_time" in self.__fields_set__:
            _dict['publishTime'] = None

        # set to None if week (nullable) is None
        # and __fields_set__ contains the field
        if self.week is None and "week" in self.__fields_set__:
            _dict['week'] = None

        # set to None if year (nullable) is None
        # and __fields_set__ contains the field
        if self.year is None and "year" in self.__fields_set__:
            _dict['year'] = None

        # set to None if output_usable (nullable) is None
        # and __fields_set__ contains the field
        if self.output_usable is None and "output_usable" in self.__fields_set__:
            _dict['outputUsable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly:
        """Create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly.parse_obj(obj)

        _obj = InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly.parse_obj({
            "dataset": obj.get("dataset"),
            "fuel_type": obj.get("fuelType"),
            "national_grid_bm_unit": obj.get("nationalGridBmUnit"),
            "bm_unit": obj.get("bmUnit"),
            "publish_time": obj.get("publishTime"),
            "week": obj.get("week"),
            "year": obj.get("year"),
            "output_usable": obj.get("outputUsable")
        })
        return _obj


