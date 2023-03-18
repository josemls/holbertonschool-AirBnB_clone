#!/usr/bin/pyhton3
"""File Storage"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Path and objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary pof objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set objects of key"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj
    
    def save(self):
        """Serialize object to JSON"""
        f_object = self.__objects
        objectdict = {obj: f_object[obj].to_dict() for obj in f_object.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objectdict, f)
    
    def reload(self):
        """Deserialize the json file."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r') as file:
                load = file.read()
                new_dict = json.loads(load)
                for key, value in new_dict.items():
                    self.__objects[key] = BaseModel(**value)
            return