# coding: utf-8

"""
    Beckn Protocol Core

    Beckn Core Transaction API specification

    The version of the OpenAPI document: 1.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from transaction.models.circle import Circle
from transaction.models.city import City
from transaction.models.country import Country
from transaction.models.descriptor import Descriptor
from transaction.models.state import State

class Location(BaseModel):
    """
    The physical location of something  # noqa: E501
    """
    id: Optional[StrictStr] = None
    descriptor: Optional[Descriptor] = None
    map_url: Optional[StrictStr] = Field(default=None, description="The url to the map of the location. This can be a globally recognized map url or the one specified by the network policy.")
    gps: Optional[constr(strict=True)] = Field(default=None, description="The GPS co-ordinates of this location.")
    address: Optional[StrictStr] = Field(default=None, description="The address of this location.")
    city: Optional[City] = Field(default=None, description="The city this location is, or is located within")
    district: Optional[StrictStr] = Field(default=None, description="The state this location is, or is located within")
    state: Optional[State] = Field(default=None, description="The state this location is, or is located within")
    country: Optional[Country] = Field(default=None, description="The country this location is, or is located within")
    area_code: Optional[StrictStr] = None
    circle: Optional[Circle] = None
    polygon: Optional[StrictStr] = Field(default=None, description="The boundary polygon of this location")
    var_3dspace: Optional[StrictStr] = Field(default=None, alias="3dspace", description="The three dimensional region describing this location")
    rating: Optional[StrictStr] = Field(default=None, description="The rating of this location")
    __properties = ["id", "descriptor", "map_url", "gps", "address", "city", "district", "state", "country", "area_code", "circle", "polygon", "3dspace", "rating"]

    @validator('gps')
    def gps_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", value):
            raise ValueError(r"must validate the regular expression /^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$/")
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
    def from_json(cls, json_str: str) -> Location:
        """Create an instance of Location from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of descriptor
        if self.descriptor:
            _dict['descriptor'] = self.descriptor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of city
        if self.city:
            _dict['city'] = self.city.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of circle
        if self.circle:
            _dict['circle'] = self.circle.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Location:
        """Create an instance of Location from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Location.parse_obj(obj)

        _obj = Location.parse_obj({
            "id": obj.get("id"),
            "descriptor": Descriptor.from_dict(obj.get("descriptor")) if obj.get("descriptor") is not None else None,
            "map_url": obj.get("map_url"),
            "gps": obj.get("gps"),
            "address": obj.get("address"),
            "city": City.from_dict(obj.get("city")) if obj.get("city") is not None else None,
            "district": obj.get("district"),
            "state": State.from_dict(obj.get("state")) if obj.get("state") is not None else None,
            "country": Country.from_dict(obj.get("country")) if obj.get("country") is not None else None,
            "area_code": obj.get("area_code"),
            "circle": Circle.from_dict(obj.get("circle")) if obj.get("circle") is not None else None,
            "polygon": obj.get("polygon"),
            "var_3dspace": obj.get("3dspace"),
            "rating": obj.get("rating")
        })
        return _obj


