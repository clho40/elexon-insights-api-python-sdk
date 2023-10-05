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

class InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow(BaseModel):
    """
    InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow
    """
    dataset: Optional[StrictStr] = None
    document_id: Optional[StrictStr] = Field(None, alias="documentId")
    document_revision_number: Optional[StrictInt] = Field(None, alias="documentRevisionNumber")
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    business_type: Optional[StrictStr] = Field(None, alias="businessType")
    year: Optional[StrictInt] = None
    month: Optional[StrictStr] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["dataset", "documentId", "documentRevisionNumber", "publishTime", "businessType", "year", "month", "amount"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow:
        """Create an instance of InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow from a JSON string"""
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

        # set to None if document_id (nullable) is None
        # and __fields_set__ contains the field
        if self.document_id is None and "document_id" in self.__fields_set__:
            _dict['documentId'] = None

        # set to None if business_type (nullable) is None
        # and __fields_set__ contains the field
        if self.business_type is None and "business_type" in self.__fields_set__:
            _dict['businessType'] = None

        # set to None if month (nullable) is None
        # and __fields_set__ contains the field
        if self.month is None and "month" in self.__fields_set__:
            _dict['month'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow:
        """Create an instance of InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow.parse_obj(obj)

        _obj = InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow.parse_obj({
            "dataset": obj.get("dataset"),
            "document_id": obj.get("documentId"),
            "document_revision_number": obj.get("documentRevisionNumber"),
            "publish_time": obj.get("publishTime"),
            "business_type": obj.get("businessType"),
            "year": obj.get("year"),
            "month": obj.get("month"),
            "amount": obj.get("amount")
        })
        return _obj


