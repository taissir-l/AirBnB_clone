#!/usr/bin/python3
"""amenity module

defines the class, Amenity() which
sub-classes the BaseModel() class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """provided by a place/house.

    Attributes:
        name
    """

    name = ""
