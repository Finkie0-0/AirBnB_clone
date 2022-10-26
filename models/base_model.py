#!/usr/bin/python3
"""Model defining the base classes for all models in our AirBnB clone project"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            del kwargs["__class__"]
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates the attribute (updated_at) with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

