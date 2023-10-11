#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""
Defines class BaseModel
"""

class BaseModel:
    """
    BaseModel
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        new_dict = {key: value for key, value in self.to_dict().items() if key != '__class__'}
        return f"[{self.__class__.__name__}] ({self.id}) {new_dict}"

    def to_dict(self):
        """
        Converts the class to a dictionary
        """

        new_dict =  {
                **self.__dict__,
                "id": BaseModel.id,
                "created_at": BaseModel.created_at,
                "updated_at": BaseModel.updated_at,
                "__class__": self.__class__.__name__
                }
        return new_dict

    def save(self):
        """
        Updates the class attribute updated_at anytime the instance of the class changes
        """
        BaseModel.updated_at = datetime.now()
