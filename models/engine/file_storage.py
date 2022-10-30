#!/usr/bin/python3
"""Contains the FileStorage class"""

import json

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    __objects = {}
    
    """Loads storage dictionary"""
    from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = { 
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review 
                  }


    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)
        
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                json_objects = json.load(f)
            for key in json_objects:
                self.__objects[key] = BaseModel(**json_objects[key])
        except Exception as e:
            print(e)

