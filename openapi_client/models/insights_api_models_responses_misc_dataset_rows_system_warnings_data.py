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
from pydantic import BaseModel, Field, StrictStr

class InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData(BaseModel):
    """
    InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData
    """
    dataset: Optional[StrictStr] = None
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    warning_text: Optional[StrictStr] = Field(None, alias="warningText")
    __properties = ["dataset", "publishTime", "warningText"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData:
        """Create an instance of InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData from a JSON string"""
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

        # set to None if warning_text (nullable) is None
        # and __fields_set__ contains the field
        if self.warning_text is None and "warning_text" in self.__fields_set__:
            _dict['warningText'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData:
        """Create an instance of InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.parse_obj(obj)

        _obj = InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.parse_obj({
            "dataset": obj.get("dataset"),
            "publish_time": obj.get("publishTime"),
            "warning_text": obj.get("warningText")
        })
        return _obj


