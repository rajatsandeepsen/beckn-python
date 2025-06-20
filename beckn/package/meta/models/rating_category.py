# coding: utf-8

"""
    Beckn Protocol Meta API

    This document contains all the meta API endpoints that are implemented by the network participants. The information returned from these endpoints typically contain cacheable information.

    The version of the OpenAPI document: 1.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class RatingCategory(str, Enum):
    """
    Category of the entity being rated
    """

    """
    allowed enum values
    """
    ITEM = 'Item'
    ORDER = 'Order'
    FULFILLMENT = 'Fulfillment'
    PROVIDER = 'Provider'
    AGENT = 'Agent'
    SUPPORT = 'Support'

    @classmethod
    def from_json(cls, json_str: str) -> RatingCategory:
        """Create an instance of RatingCategory from a JSON string"""
        return RatingCategory(json.loads(json_str))


