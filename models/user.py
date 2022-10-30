#!/usr/bin/python3
""" The User class """

from models.base_model import BaseModel

class User(BaseModel):
     """Representation of a user """
     email = ""
     password = ""
     first_name = ""
     last_name = ""
