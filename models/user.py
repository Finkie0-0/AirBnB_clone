#!/usr/bin/python3
""" The User class """

import models
from models.base_model import BaseModel

class User(BaseModel):
     """Representation of a user """
     def __init__(self, *args, **kwargs):
         """Initializ the user"""
         if len(kwargs) == 0:
             self.email = ""
             self.password = ""
             self.first_name = ""
             self.last_name = ""
         super().__init__(*args, **Kwargs)

