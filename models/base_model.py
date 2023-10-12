#!/usr/bin/python3
"""
Defines class BaseModel
"""
from uuid import uuid4
from datetime import datetime
from . import storage


class BaseModel:
    """
    BaseModel
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance with the dictionary respresentation
        """
        if not kwargs:
            BaseModel.id = str(uuid4())
            BaseModel.created_at = datetime.now()
            BaseModel.updated_at = datetime.now()
            storage.new(self.to_dict())  # add the obj for saving to json file later
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(BaseModel, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        new_dict = {key: value for key, value in self.to_dict().items() if key != '__class__'}
        parsed_time_dict = {**new_dict}
        for key, value in new_dict.items():
            if key == 'created_at' or key == 'updated_at':
                value = datetime.fromisoformat(value).strftime("datetime.datetime(%Y, %m, %d, %H, %M, %S, %f)")
                parsed_time_dict[key] = value
        return f"[{self.__class__.__name__}] ({self.id}) {parsed_time_dict}"

    def to_dict(self):
        """
        Converts the class to a dictionary
        """

        new_dict =  {
                **self.__dict__,
                "id": BaseModel.id,
                "created_at": BaseModel.created_at.isoformat(),
                "updated_at": BaseModel.updated_at.isoformat(),
                "__class__": self.__class__.__name__
                }
        return new_dict

    def save(self):
        """
        Updates the class attribute updated_at anytime the instance of the class changes
        """
        BaseModel.updated_at = datetime.now()
        storage.save() # save the instances to json file
