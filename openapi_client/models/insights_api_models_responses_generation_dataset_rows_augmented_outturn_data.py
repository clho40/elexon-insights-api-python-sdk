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

class InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData(BaseModel):
    """
    InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData
    """
    dataset: Optional[StrictStr] = None
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    start_time: Optional[datetime] = Field(None, alias="startTime")
    settlement_date: Optional[date] = Field(None, alias="settlementDate")
    settlement_period: Optional[StrictInt] = Field(None, alias="settlementPeriod")
    fuel_type: Optional[StrictStr] = Field(None, alias="fuelType")
    generation: Optional[StrictInt] = None
    __properties = ["dataset", "publishTime", "startTime", "settlementDate", "settlementPeriod", "fuelType", "generation"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData:
        """Create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData from a JSON string"""
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

        # set to None if start_time (nullable) is None
        # and __fields_set__ contains the field
        if self.start_time is None and "start_time" in self.__fields_set__:
            _dict['startTime'] = None

        # set to None if settlement_date (nullable) is None
        # and __fields_set__ contains the field
        if self.settlement_date is None and "settlement_date" in self.__fields_set__:
            _dict['settlementDate'] = None

        # set to None if settlement_period (nullable) is None
        # and __fields_set__ contains the field
        if self.settlement_period is None and "settlement_period" in self.__fields_set__:
            _dict['settlementPeriod'] = None

        # set to None if fuel_type (nullable) is None
        # and __fields_set__ contains the field
        if self.fuel_type is None and "fuel_type" in self.__fields_set__:
            _dict['fuelType'] = None

        # set to None if generation (nullable) is None
        # and __fields_set__ contains the field
        if self.generation is None and "generation" in self.__fields_set__:
            _dict['generation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData:
        """Create an instance of InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData.parse_obj(obj)

        _obj = InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData.parse_obj({
            "dataset": obj.get("dataset"),
            "publish_time": obj.get("publishTime"),
            "start_time": obj.get("startTime"),
            "settlement_date": obj.get("settlementDate"),
            "settlement_period": obj.get("settlementPeriod"),
            "fuel_type": obj.get("fuelType"),
            "generation": obj.get("generation")
        })
        return _obj

