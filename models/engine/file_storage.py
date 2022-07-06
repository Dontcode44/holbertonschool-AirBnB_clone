#!/usr/bin/python3
import json
import os.path as path
"""holbertonschool-AirBnB_clone - file_storage"""


class FileStorage():
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""
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
        data = {}
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as save:
                data = json.load(save)
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as save:
            data.update(new_dict)
            json.dump(data, save)

    def reload(self):
        """reload - deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as save:
                return json.loads(save.read())
        pass
