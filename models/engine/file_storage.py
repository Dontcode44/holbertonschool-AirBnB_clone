#!/usr/bin/python3
import json
import os.path as path
from models.base_model import BaseModel
from models.user import User

"""holbertonschool-AirBnB_clone - file_storage"""


class FileStorage():
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """new - sets in __objects the obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """save - writes an Object to a text file"""
        new_dict = {}
        with open(self.__file_path, 'w') as save:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, save)

    def reload(self):
        """reload - deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(FileStorage.__file_path, "r") as save:
                for key, value in json.load(save).items():
                    self.__objects[key] = (FileStorage.
                                           classes[value["__class__"]]
                                           (**value))
