#!/usr/bin/python3
"""
The module defines class State that models
a State object
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    class State that inherits from BaseModel
    Attrs:
        name (str): Public class attribute to store
        the name of the state
    """
    name = ""
