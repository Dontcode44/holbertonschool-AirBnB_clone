#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""holbertonschool-AirBnB_clone"""


class BaseModel():
    """BaseModel - class for all common attributes/methods"""
    def __init__(self, id=None):
        """__init__ - inicialize the attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat("T", "microseconds")
        self.updated_at = datetime.now().isoformat("T", "microseconds")
    
    def __str__(self):
        """__str__ - print class name, id and dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save - updates the public instance attribute updated_at"""
        self.updated_at = datetime.now().isoformat("T", "microseconds")
        
    def to_dict(self):
        """to_dict - returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
#2022-07-01T18:15:47.144062