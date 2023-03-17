#!/usr/bin/pyhton3
"""File Storage"""

import json


class FileStorage:
    """Path and objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary pof objects"""
        return self.__objects
    
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
        """Deserialize the JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                obj_dir = json.loads(f.read())
                for key, value in obj_dir.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass