#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
define a class
"""


class Rectangle(BaseGeometry):
    """
    nherits from BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
