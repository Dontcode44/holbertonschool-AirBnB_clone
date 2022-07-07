#!/usr/bin/python3
import json
import os.path as path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""holbertonschool-AirBnB_clone - file_storage"""


class FileStorage():
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""
    classes = {"BaseModel": BaseModel, "User": User}
    __file_path = 'file.json'
    __objects = {}

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
        all_obj = {}
        if path.exists(FileStorage.__file_path):
            all_obj = self.read_json()
        for key, value in all_obj.items():
            keys = FileStorage.__objects
            keys[key] = FileStorage.classes[value["__class__"]](**value)
        pass

    def read_json(self):
        """read json file"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as save:
                return json.load(save)
        else:
            with open(self.__file_path, 'w') as save:
                json.dump({}, save)
            return {}
