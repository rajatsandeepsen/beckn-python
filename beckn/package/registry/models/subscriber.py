# coding: utf-8

"""
    Beckn Protocol Registry Infrastructure API

    This document contains the API specification for the Registry infrastructure of a beckn-enabled network. The Registry API forms the trust layer of beckn protocol. When implemented, they enable creation of an infrastructure that allow trusted transactions between network participants to take place by means of digital signature authentication. The core infrastructure is called the Network Registry or simply, Registry. Any network participant that is listed on the registry can be assumed to have successfully passed the certfication and compliance process of the network, and hence be trusted to transact with.

    The version of the OpenAPI document: 1.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from registry.models.location import Location

class Subscriber(BaseModel):
    """
    A unique operational configuration of a trusted platform on a network.  # noqa: E501
    """
    subscriber_id: Optional[StrictStr] = Field(default=None, description="A globally unique identifier of the platform, Typically it is the fully qualified domain name (FQDN) of the platform.")
    url: Optional[StrictStr] = Field(default=None, description="The callback URL of the Subscriber. This should necessarily contain the same domain name as set in `subscriber_id``.")
    type: Optional[StrictStr] = Field(default=None, description="The role of subscriber on the network")
    domain: Optional[Any] = Field(default=None, description="Operating industry domain that this subscriber offers its products or services in. A single subscriber can operate in multiple domains. Each operating domain must have a unique subscriber object entry in the req")
    location: Optional[Location] = Field(default=None, description="The region of operation of this subscriber")
    __properties = ["subscriber_id", "url", "type", "domain", "location"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BAP', 'BPP', 'BG',):
            raise ValueError("must be one of enum values ('BAP', 'BPP', 'BG')")
        return value

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
    def from_json(cls, json_str: str) -> Subscriber:
        """Create an instance of Subscriber from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if domain (nullable) is None
        # and __fields_set__ contains the field
        if self.domain is None and "domain" in self.__fields_set__:
            _dict['domain'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Subscriber:
        """Create an instance of Subscriber from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Subscriber.parse_obj(obj)

        _obj = Subscriber.parse_obj({
            "subscriber_id": obj.get("subscriber_id"),
            "url": obj.get("url"),
            "type": obj.get("type"),
            "domain": obj.get("domain"),
            "location": Location.from_dict(obj.get("location")) if obj.get("location") is not None else None
        })
        return _obj


