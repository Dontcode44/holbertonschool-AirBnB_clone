#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models
"""holbertonschool-AirBnB_clone"""


class BaseModel():
    """BaseModel - class for all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        """__init__ - inicialize the attributes"""
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "id":
                    self.id = str(value)
                elif key == "created_at":
                    self.created_at = (datetime.
                                       strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "updated_at":
                    self.updated_at = (datetime.
                                       strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__ - print class name, id and dict"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save - updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict - returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict.update({"__class__": self.__class__.__name__})
        new_dict.update({"created_at": self.created_at.isoformat()})
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        self.__dict__["__class__"] = self.__class__.__name__
        return new_dict
