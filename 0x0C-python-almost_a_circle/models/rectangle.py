#!/usr/bin/python3
"""
Define Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    representing a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initilize attributes

        width: width of rectangle
        Height: height of rectangle
        x: x coordinates
        y: y coordinates
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ retrieve width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """

