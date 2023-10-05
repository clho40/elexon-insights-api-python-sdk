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


from typing import List, Optional
from pydantic import BaseModel, conlist
from openapi_client.models.insights_api_models_metadata_api_response_source_metadata import InsightsApiModelsMetadataApiResponseSourceMetadata
from openapi_client.models.insights_api_models_responses_balancing_balancing_services_volume import InsightsApiModelsResponsesBalancingBalancingServicesVolume

class InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume(BaseModel):
    """
    InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume
    """
    data: Optional[conlist(InsightsApiModelsResponsesBalancingBalancingServicesVolume)] = None
    metadata: Optional[InsightsApiModelsMetadataApiResponseSourceMetadata] = None
    __properties = ["data", "metadata"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume:
        """Create an instance of InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume:
        """Create an instance of InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume.parse_obj(obj)

        _obj = InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume.parse_obj({
            "data": [InsightsApiModelsResponsesBalancingBalancingServicesVolume.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "metadata": InsightsApiModelsMetadataApiResponseSourceMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None
        })
        return _obj


