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
from pydantic import BaseModel
from transaction.models.item_quantity_allocated import ItemQuantityAllocated
from transaction.models.item_quantity_available import ItemQuantityAvailable
from transaction.models.item_quantity_maximum import ItemQuantityMaximum
from transaction.models.item_quantity_minimum import ItemQuantityMinimum
from transaction.models.item_quantity_selected import ItemQuantitySelected
from transaction.models.item_quantity_unitized import ItemQuantityUnitized

class ItemQuantity(BaseModel):
    """
    Describes the count or amount of an item  # noqa: E501
    """
    allocated: Optional[ItemQuantityAllocated] = None
    available: Optional[ItemQuantityAvailable] = None
    maximum: Optional[ItemQuantityMaximum] = None
    minimum: Optional[ItemQuantityMinimum] = None
    selected: Optional[ItemQuantitySelected] = None
    unitized: Optional[ItemQuantityUnitized] = None
    __properties = ["allocated", "available", "maximum", "minimum", "selected", "unitized"]

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
    def from_json(cls, json_str: str) -> ItemQuantity:
        """Create an instance of ItemQuantity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of allocated
        if self.allocated:
            _dict['allocated'] = self.allocated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available
        if self.available:
            _dict['available'] = self.available.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum
        if self.maximum:
            _dict['maximum'] = self.maximum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minimum
        if self.minimum:
            _dict['minimum'] = self.minimum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selected
        if self.selected:
            _dict['selected'] = self.selected.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unitized
        if self.unitized:
            _dict['unitized'] = self.unitized.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ItemQuantity:
        """Create an instance of ItemQuantity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ItemQuantity.parse_obj(obj)

        _obj = ItemQuantity.parse_obj({
            "allocated": ItemQuantityAllocated.from_dict(obj.get("allocated")) if obj.get("allocated") is not None else None,
            "available": ItemQuantityAvailable.from_dict(obj.get("available")) if obj.get("available") is not None else None,
            "maximum": ItemQuantityMaximum.from_dict(obj.get("maximum")) if obj.get("maximum") is not None else None,
            "minimum": ItemQuantityMinimum.from_dict(obj.get("minimum")) if obj.get("minimum") is not None else None,
            "selected": ItemQuantitySelected.from_dict(obj.get("selected")) if obj.get("selected") is not None else None,
            "unitized": ItemQuantityUnitized.from_dict(obj.get("unitized")) if obj.get("unitized") is not None else None
        })
        return _obj


