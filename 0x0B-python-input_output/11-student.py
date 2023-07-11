#!/usr/bin/python3
"""
defien clss Student
"""


class Student:
    """
    define class student with requirement
    """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """ serilize """
        if (type(attrs) == list and all(type(att) == str for att in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replace all attr """
        for n, v in json.items():
            setattr(self, n, v)
