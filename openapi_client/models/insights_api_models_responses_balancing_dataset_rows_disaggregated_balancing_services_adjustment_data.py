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

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData(BaseModel):
    """
    InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData
    """
    dataset: Optional[StrictStr] = None
    settlement_date: Optional[date] = Field(None, alias="settlementDate")
    settlement_period: Optional[StrictInt] = Field(None, alias="settlementPeriod")
    id: Optional[StrictInt] = None
    cost: Optional[Union[StrictFloat, StrictInt]] = None
    volume: Optional[Union[StrictFloat, StrictInt]] = None
    so_flag: Optional[StrictBool] = Field(None, alias="soFlag")
    stor_flag: Optional[StrictBool] = Field(None, alias="storFlag")
    party_id: Optional[StrictStr] = Field(None, alias="partyId")
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    is_tendered: Optional[StrictBool] = Field(None, alias="isTendered")
    service: Optional[StrictStr] = None
    __properties = ["dataset", "settlementDate", "settlementPeriod", "id", "cost", "volume", "soFlag", "storFlag", "partyId", "assetId", "isTendered", "service"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData:
        """Create an instance of InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData from a JSON string"""
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

        # set to None if cost (nullable) is None
        # and __fields_set__ contains the field
        if self.cost is None and "cost" in self.__fields_set__:
            _dict['cost'] = None

        # set to None if party_id (nullable) is None
        # and __fields_set__ contains the field
        if self.party_id is None and "party_id" in self.__fields_set__:
            _dict['partyId'] = None

        # set to None if asset_id (nullable) is None
        # and __fields_set__ contains the field
        if self.asset_id is None and "asset_id" in self.__fields_set__:
            _dict['assetId'] = None

        # set to None if is_tendered (nullable) is None
        # and __fields_set__ contains the field
        if self.is_tendered is None and "is_tendered" in self.__fields_set__:
            _dict['isTendered'] = None

        # set to None if service (nullable) is None
        # and __fields_set__ contains the field
        if self.service is None and "service" in self.__fields_set__:
            _dict['service'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData:
        """Create an instance of InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData.parse_obj(obj)

        _obj = InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData.parse_obj({
            "dataset": obj.get("dataset"),
            "settlement_date": obj.get("settlementDate"),
            "settlement_period": obj.get("settlementPeriod"),
            "id": obj.get("id"),
            "cost": obj.get("cost"),
            "volume": obj.get("volume"),
            "so_flag": obj.get("soFlag"),
            "stor_flag": obj.get("storFlag"),
            "party_id": obj.get("partyId"),
            "asset_id": obj.get("assetId"),
            "is_tendered": obj.get("isTendered"),
            "service": obj.get("service")
        })
        return _obj


