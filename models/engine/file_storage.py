#!/usr/bin/python3
"""
The module contains FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    The class is responsible for serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the private class attribute "objects"
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a given object to the dictionary __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects attribute to the JSON file
        """
        to_json = {key: value.to_dict() for key, value
                   in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w") as file:
            json.dump(to_json, file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects attribute
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)

            if data:
                for key, value in data.items():
                    FileStorage.__objects[key] = BaseModel(**value)

        except (FileNotFoundError, ValueError):
            pass
