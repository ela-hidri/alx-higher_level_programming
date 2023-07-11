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

    def to_json(self):
        """ serilize """
        return self.__dict__
