#!/usr/bin/python3
"""
the module file_storage.py

defines a FileStorage class.
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage():
    """JSON file and deserializes JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """it returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """it sets in __objects obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        JSON file to __objects only if the JSON
        if file exists; otherwise, does nothing
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
