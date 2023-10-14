#!/usr/bin/python3
"""
The module defines class Amenity that models
a Amenity object
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    class Amenity that inherits from BaseModel
    Attrs:
        name (str): Public class attribute to store
                    the name of the amenity
    """
    name = ""
