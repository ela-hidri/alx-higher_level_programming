#!/usr/bin/python3
"""
Define Base class
"""
import json
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file: """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                ll = [att.to_dictionary() for att in list_objs]
                f.write(Base.to_json_string(ll))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string: """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            new_class = cls(1, 1)
        else:
            new_class = cls(1)
        new_class.update(**dictionary)
        return new_class

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = str(cls.__name__) + ".json"
        if os.path.isfile(filename) is False:
            return []
        with open(filename, mode="r", encoding="utf-8") as f:
            content = Base.from_json_string(f.read())
            return [cls.create(**dictin) for dictin in content]
