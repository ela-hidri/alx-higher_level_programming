#!/usr/bin/python3
"""
define a class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    nherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialise var

        Args:
            self: class
            Width: width of rectangle
            height: height of rectangle
        Return:
            nothing
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        return the area of rect
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        printf [Rectangle] <width>/<height>
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
