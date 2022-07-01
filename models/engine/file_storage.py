#!/usr/bin/python3
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
        pass
    def save(self):
        pass
    def reload(self):
        pass
    