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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData(BaseModel):
    """
    InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData
    """
    dataset: Optional[StrictStr] = None
    settlement_date: Optional[date] = Field(None, alias="settlementDate")
    settlement_period: Optional[StrictInt] = Field(None, alias="settlementPeriod")
    time: Optional[datetime] = None
    notice: Optional[StrictInt] = None
    national_grid_bm_unit: Optional[StrictStr] = Field(None, alias="nationalGridBmUnit")
    bm_unit: Optional[StrictStr] = Field(None, alias="bmUnit")
    __properties = ["dataset", "settlementDate", "settlementPeriod", "time", "notice", "nationalGridBmUnit", "bmUnit"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData:
        """Create an instance of InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData from a JSON string"""
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

        # set to None if national_grid_bm_unit (nullable) is None
        # and __fields_set__ contains the field
        if self.national_grid_bm_unit is None and "national_grid_bm_unit" in self.__fields_set__:
            _dict['nationalGridBmUnit'] = None

        # set to None if bm_unit (nullable) is None
        # and __fields_set__ contains the field
        if self.bm_unit is None and "bm_unit" in self.__fields_set__:
            _dict['bmUnit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData:
        """Create an instance of InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData.parse_obj(obj)

        _obj = InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData.parse_obj({
            "dataset": obj.get("dataset"),
            "settlement_date": obj.get("settlementDate"),
            "settlement_period": obj.get("settlementPeriod"),
            "time": obj.get("time"),
            "notice": obj.get("notice"),
            "national_grid_bm_unit": obj.get("nationalGridBmUnit"),
            "bm_unit": obj.get("bmUnit")
        })
        return _obj


