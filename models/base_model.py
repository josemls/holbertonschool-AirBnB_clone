#!/usr/bin/python3
"""BaseModel"""

import uuid
from datetime import datetime
import models


"""date and time"""
dtm = "%Y-%m-%dT%H:%M:%S.%f"
value = "2017-06-14T22:31:03.285259"

class BaseModel:
    """class that defines attributes for other classes"""

    def __init__(self, *args, **kwargs):
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
        return "[{}] ({}) {}" .format(self.__class__.__name__,
                                      self.id, self.__dict__)
    
    def save(self):
        """Update instance attribute with date and hour"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """Return a dictionary that contains all keys"""
        dic = {

            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.strftime(dtm),
            'id': self.id,
            'created_at': self.created_at.strftime(dtm),
        }
        return dic