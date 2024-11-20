#!/usr/bin/python3

import uuid
from datetime import datetime

class Basemodel:
    """Basemodel that defines all common attributes/methods for other classes"""

    def __init__(self):
        """initializes an instance of Basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.current()
        self.updated_at = datetime.current()

    def save(self):
        """updates public instance attribute with current datetime"""
        self.updated_at = datetime.current()

    def to_dict(self):
        """returns a dict containing all keys of __dict__"""
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()

        return object_dict

    def __str__(self):
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format{class_name. self.id. self.__dict__}