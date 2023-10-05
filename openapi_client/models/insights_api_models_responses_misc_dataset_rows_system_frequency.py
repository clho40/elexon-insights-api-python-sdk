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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency(BaseModel):
    """
    InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency
    """
    dataset: Optional[StrictStr] = None
    measurement_time: Optional[datetime] = Field(None, alias="measurementTime")
    frequency: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["dataset", "measurementTime", "frequency"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency:
        """Create an instance of InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency:
        """Create an instance of InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency.parse_obj(obj)

        _obj = InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency.parse_obj({
            "dataset": obj.get("dataset"),
            "measurement_time": obj.get("measurementTime"),
            "frequency": obj.get("frequency")
        })
        return _obj


