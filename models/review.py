#!/usr/bin/python3
"""
The module defines class Review that models
a Review object
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    class Review that inherits from BaseModel
    Attrs:
        place_id (str): Public class attribute to store the
                        place id
        user_id (str): Public class attribute to store
                    the user id
        text (str): Public class attr to store the review text
    """
    place_id = ""
    user_id = ""
    text = ""
