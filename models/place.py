#!/usr/bin/python3
"""
The module defines class Place that models
a Place object
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    class Place that inherits from BaseModel
    Attrs:
        city_id (str): Public class attribute to store the
                        city id
        user_id (str): Public class attr to store the user id
        name (str): Public class attr to store place name
        description (str): Public class attr to store
                           place descritpion
        number_rooms (int): Public class attr to store no of rooms
        number_bathrooms (int): Public class attr to store no
                                of bathrooms
        max_guest (int): Public class attr to store no. of guest
                         that can be accommodated
        price_by_night (int): Public class attr to store the
                              price charges for a night
        latitude (float): Public class attr to store the latitude
                          of the place
        longitude (float): Public class attr to store the
                           longitude of the place
        amenity_ids (list): Public class attr to store list of
                            Amenity id
    """
    state_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
