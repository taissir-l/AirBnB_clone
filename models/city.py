#!/usr/bin/python3
"""city module

defines class of City()
"""
from models.base_model import BaseModel


class City(BaseModel):
    """city in app

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
