#!/usr/bin/python3
"""BaseModel"""

import uuid
from datetime import datetime
import models
import json


"""date and time"""
dateformat = "%Y-%m-%dT%H:%M:%S.%f"
value = "2017-06-14T22:31:03.285259"

class BaseModel:
    """class that defines attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Instances of the base model.
            id: unique identification.
            created_at: datetime - datetime when an instance is created.
            updated_at: datetime - datetime when an instance is modified.
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:        
            self.id = str(uuid.uuid4)
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Print name, id and dictionary"""
        return "[{}] ({}) {}" .format(self.__class__.__name__,self.id, self.__dict__)
                        
    def save(self):
        """Update instance attribute with date and hour"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """Return a dictionary that contains all keys"""
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict