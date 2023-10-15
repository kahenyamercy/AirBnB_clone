#!/usr/bin/python3
"""
The module defines class City that models
a City object
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    class City that inherits from BaseModel
    Attrs:
        state_id (str): Public class attribute to store the
                        state id
        name (str): Public class attribute to store
                    the name of the city
    """
    state_id = ""
    name = ""
