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
from pydantic import BaseModel, Field
from transaction.models.error import Error
from transaction.models.on_confirm_context import OnConfirmContext
from transaction.models.select_message import SelectMessage

class OnConfirm(BaseModel):
    """
    OnConfirm
    """
    context: OnConfirmContext = Field(...)
    message: Optional[SelectMessage] = None
    error: Optional[Error] = None
    __properties = ["context", "message", "error"]

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
    def from_json(cls, json_str: str) -> OnConfirm:
        """Create an instance of OnConfirm from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OnConfirm:
        """Create an instance of OnConfirm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OnConfirm.parse_obj(obj)

        _obj = OnConfirm.parse_obj({
            "context": OnConfirmContext.from_dict(obj.get("context")) if obj.get("context") is not None else None,
            "message": SelectMessage.from_dict(obj.get("message")) if obj.get("message") is not None else None,
            "error": Error.from_dict(obj.get("error")) if obj.get("error") is not None else None
        })
        return _obj


