#!/usr/bin/python3
"""review module.

defines the class Review()
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """reviews of a place or house

    It is a review posted by the users

    Attributes:
        text
        user_id
        place_id
    """
    text = ""
    user_id = ""
    place_id = ""
