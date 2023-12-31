#!/usr/bin/python3
"""
The module contains FileStorage class
"""
from json import load, dump, JSONDecodeError
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Add a given object to the dictionary __objects
        """
        inst = obj.__class__.__name__
        idO = obj.id
        key = "{}.{}".format(inst, idO)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects attribute to the JSON file
        """
        insstances = FileStorage.__objects
        insstances_dict = {key: insstances[key].to_dict()
                           for key in insstances.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dump(insstances_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects attribute
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                inst = load(file)
                for key, value in inst.items():
                    class_name = inst[key]["__class__"]
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except (FileNotFoundError, JSONDecodeError):
            pass
