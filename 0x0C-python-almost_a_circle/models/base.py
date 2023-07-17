#!/usr/bin/python3
"""
Define Base class
"""
import json


class Base:
    """
    representing the base of all classes

    Attributes:
        nb_objects: number of instantiated bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initailizing attributes

        Args:
        id: id of base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """ 
        returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
