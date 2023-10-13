#!/usr/bin/python3
"""
This modele defines class User that inherits from
the BaseModel class
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel

    Attrs:
        email (str): Public class attribute to store user email
        password (str): Public class attribute to store
                        user password
        first_name (str): Public class attribute to store
                          user first name
        last_name (str): Public class attribute to store
                         user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
