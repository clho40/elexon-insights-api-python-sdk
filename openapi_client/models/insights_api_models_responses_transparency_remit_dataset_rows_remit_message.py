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
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from openapi_client.models.insights_api_models_responses_transparency_remit_dataset_rows_outage_profile_data import InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData

class InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage(BaseModel):
    """
    InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage
    """
    dataset: Optional[StrictStr] = None
    mrid: Optional[StrictStr] = None
    revision_number: Optional[StrictInt] = Field(None, alias="revisionNumber")
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    created_time: Optional[datetime] = Field(None, alias="createdTime")
    message_type: Optional[StrictStr] = Field(None, alias="messageType")
    message_heading: Optional[StrictStr] = Field(None, alias="messageHeading")
    event_type: Optional[StrictStr] = Field(None, alias="eventType")
    unavailability_type: Optional[StrictStr] = Field(None, alias="unavailabilityType")
    participant_id: Optional[StrictStr] = Field(None, alias="participantId")
    registration_code: Optional[StrictStr] = Field(None, alias="registrationCode")
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    asset_type: Optional[StrictStr] = Field(None, alias="assetType")
    affected_unit: Optional[StrictStr] = Field(None, alias="affectedUnit")
    affected_unit_eic: Optional[StrictStr] = Field(None, alias="affectedUnitEIC")
    affected_area: Optional[StrictStr] = Field(None, alias="affectedArea")
    bidding_zone: Optional[StrictStr] = Field(None, alias="biddingZone")
    fuel_type: Optional[StrictStr] = Field(None, alias="fuelType")
    normal_capacity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="normalCapacity")
    available_capacity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="availableCapacity")
    unavailable_capacity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="unavailableCapacity")
    event_status: Optional[StrictStr] = Field(None, alias="eventStatus")
    event_start_time: Optional[datetime] = Field(None, alias="eventStartTime")
    event_end_time: Optional[datetime] = Field(None, alias="eventEndTime")
    duration_uncertainty: Optional[StrictStr] = Field(None, alias="durationUncertainty")
    cause: Optional[StrictStr] = None
    related_information: Optional[StrictStr] = Field(None, alias="relatedInformation")
    outage_profile: Optional[conlist(InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData)] = Field(None, alias="outageProfile")
    __properties = ["dataset", "mrid", "revisionNumber", "publishTime", "createdTime", "messageType", "messageHeading", "eventType", "unavailabilityType", "participantId", "registrationCode", "assetId", "assetType", "affectedUnit", "affectedUnitEIC", "affectedArea", "biddingZone", "fuelType", "normalCapacity", "availableCapacity", "unavailableCapacity", "eventStatus", "eventStartTime", "eventEndTime", "durationUncertainty", "cause", "relatedInformation", "outageProfile"]

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
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage:
        """Create an instance of InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in outage_profile (list)
        _items = []
        if self.outage_profile:
            for _item in self.outage_profile:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outageProfile'] = _items
        # set to None if dataset (nullable) is None
        # and __fields_set__ contains the field
        if self.dataset is None and "dataset" in self.__fields_set__:
            _dict['dataset'] = None

        # set to None if mrid (nullable) is None
        # and __fields_set__ contains the field
        if self.mrid is None and "mrid" in self.__fields_set__:
            _dict['mrid'] = None

        # set to None if message_type (nullable) is None
        # and __fields_set__ contains the field
        if self.message_type is None and "message_type" in self.__fields_set__:
            _dict['messageType'] = None

        # set to None if message_heading (nullable) is None
        # and __fields_set__ contains the field
        if self.message_heading is None and "message_heading" in self.__fields_set__:
            _dict['messageHeading'] = None

        # set to None if event_type (nullable) is None
        # and __fields_set__ contains the field
        if self.event_type is None and "event_type" in self.__fields_set__:
            _dict['eventType'] = None

        # set to None if unavailability_type (nullable) is None
        # and __fields_set__ contains the field
        if self.unavailability_type is None and "unavailability_type" in self.__fields_set__:
            _dict['unavailabilityType'] = None

        # set to None if participant_id (nullable) is None
        # and __fields_set__ contains the field
        if self.participant_id is None and "participant_id" in self.__fields_set__:
            _dict['participantId'] = None

        # set to None if registration_code (nullable) is None
        # and __fields_set__ contains the field
        if self.registration_code is None and "registration_code" in self.__fields_set__:
            _dict['registrationCode'] = None

        # set to None if asset_id (nullable) is None
        # and __fields_set__ contains the field
        if self.asset_id is None and "asset_id" in self.__fields_set__:
            _dict['assetId'] = None

        # set to None if asset_type (nullable) is None
        # and __fields_set__ contains the field
        if self.asset_type is None and "asset_type" in self.__fields_set__:
            _dict['assetType'] = None

        # set to None if affected_unit (nullable) is None
        # and __fields_set__ contains the field
        if self.affected_unit is None and "affected_unit" in self.__fields_set__:
            _dict['affectedUnit'] = None

        # set to None if affected_unit_eic (nullable) is None
        # and __fields_set__ contains the field
        if self.affected_unit_eic is None and "affected_unit_eic" in self.__fields_set__:
            _dict['affectedUnitEIC'] = None

        # set to None if affected_area (nullable) is None
        # and __fields_set__ contains the field
        if self.affected_area is None and "affected_area" in self.__fields_set__:
            _dict['affectedArea'] = None

        # set to None if bidding_zone (nullable) is None
        # and __fields_set__ contains the field
        if self.bidding_zone is None and "bidding_zone" in self.__fields_set__:
            _dict['biddingZone'] = None

        # set to None if fuel_type (nullable) is None
        # and __fields_set__ contains the field
        if self.fuel_type is None and "fuel_type" in self.__fields_set__:
            _dict['fuelType'] = None

        # set to None if normal_capacity (nullable) is None
        # and __fields_set__ contains the field
        if self.normal_capacity is None and "normal_capacity" in self.__fields_set__:
            _dict['normalCapacity'] = None

        # set to None if available_capacity (nullable) is None
        # and __fields_set__ contains the field
        if self.available_capacity is None and "available_capacity" in self.__fields_set__:
            _dict['availableCapacity'] = None

        # set to None if unavailable_capacity (nullable) is None
        # and __fields_set__ contains the field
        if self.unavailable_capacity is None and "unavailable_capacity" in self.__fields_set__:
            _dict['unavailableCapacity'] = None

        # set to None if event_status (nullable) is None
        # and __fields_set__ contains the field
        if self.event_status is None and "event_status" in self.__fields_set__:
            _dict['eventStatus'] = None

        # set to None if event_end_time (nullable) is None
        # and __fields_set__ contains the field
        if self.event_end_time is None and "event_end_time" in self.__fields_set__:
            _dict['eventEndTime'] = None

        # set to None if duration_uncertainty (nullable) is None
        # and __fields_set__ contains the field
        if self.duration_uncertainty is None and "duration_uncertainty" in self.__fields_set__:
            _dict['durationUncertainty'] = None

        # set to None if cause (nullable) is None
        # and __fields_set__ contains the field
        if self.cause is None and "cause" in self.__fields_set__:
            _dict['cause'] = None

        # set to None if related_information (nullable) is None
        # and __fields_set__ contains the field
        if self.related_information is None and "related_information" in self.__fields_set__:
            _dict['relatedInformation'] = None

        # set to None if outage_profile (nullable) is None
        # and __fields_set__ contains the field
        if self.outage_profile is None and "outage_profile" in self.__fields_set__:
            _dict['outageProfile'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage:
        """Create an instance of InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage.parse_obj(obj)

        _obj = InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage.parse_obj({
            "dataset": obj.get("dataset"),
            "mrid": obj.get("mrid"),
            "revision_number": obj.get("revisionNumber"),
            "publish_time": obj.get("publishTime"),
            "created_time": obj.get("createdTime"),
            "message_type": obj.get("messageType"),
            "message_heading": obj.get("messageHeading"),
            "event_type": obj.get("eventType"),
            "unavailability_type": obj.get("unavailabilityType"),
            "participant_id": obj.get("participantId"),
            "registration_code": obj.get("registrationCode"),
            "asset_id": obj.get("assetId"),
            "asset_type": obj.get("assetType"),
            "affected_unit": obj.get("affectedUnit"),
            "affected_unit_eic": obj.get("affectedUnitEIC"),
            "affected_area": obj.get("affectedArea"),
            "bidding_zone": obj.get("biddingZone"),
            "fuel_type": obj.get("fuelType"),
            "normal_capacity": obj.get("normalCapacity"),
            "available_capacity": obj.get("availableCapacity"),
            "unavailable_capacity": obj.get("unavailableCapacity"),
            "event_status": obj.get("eventStatus"),
            "event_start_time": obj.get("eventStartTime"),
            "event_end_time": obj.get("eventEndTime"),
            "duration_uncertainty": obj.get("durationUncertainty"),
            "cause": obj.get("cause"),
            "related_information": obj.get("relatedInformation"),
            "outage_profile": [InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData.from_dict(_item) for _item in obj.get("outageProfile")] if obj.get("outageProfile") is not None else None
        })
        return _obj


