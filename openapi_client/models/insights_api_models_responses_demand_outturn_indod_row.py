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

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class InsightsApiModelsResponsesDemandOutturnIndodRow(BaseModel):
    """
    InsightsApiModelsResponsesDemandOutturnIndodRow
    """
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    settlement_date: Optional[date] = Field(None, alias="settlementDate")
    demand: Optional[StrictInt] = None
    __properties = ["publishTime", "settlementDate", "demand"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesDemandOutturnIndodRow:
        """Create an instance of InsightsApiModelsResponsesDemandOutturnIndodRow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if demand (nullable) is None
        # and __fields_set__ contains the field
        if self.demand is None and "demand" in self.__fields_set__:
            _dict['demand'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesDemandOutturnIndodRow:
        """Create an instance of InsightsApiModelsResponsesDemandOutturnIndodRow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesDemandOutturnIndodRow.parse_obj(obj)

        _obj = InsightsApiModelsResponsesDemandOutturnIndodRow.parse_obj({
            "publish_time": obj.get("publishTime"),
            "settlement_date": obj.get("settlementDate"),
            "demand": obj.get("demand")
        })
        return _obj


