#!/usr/bin/python3
"""
The module contains BaseModel template (class)
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The base class for all classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization method
        """
        self.id = str(uuid.uui4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
         else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of an instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public attribute "updated_at"
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all the instance
        attributes and its class name
        """
        attrs = self.__dict__.copy()
        attrs["__class__"] = self.__class__.__name__
        attrs["created_at"] = self.created_at.isoformat()
        attrs["updated_at"] = self.updated_at.isoformat()
        return attrs
