#!/usr/bin/python3
"""BaseModel"""

import uuid
from datetime import datetime
import models

dtm = "%Y-%m-%dT%H:%M:%S.%f"
value = "2017-06-14T22:31:03.285259"

class BaseModel:
    """class that defines attributes for other classes"""

    def __init__(self):
        #assign id
        self.id = str(uuid.uuid4)
        #Assign date
        self.created_at = datetime.now()
        #update the date
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