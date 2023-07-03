#!/usr/bin/python3
# 2-rectangle.py
""" defines a rectangle """


class Rectangle():
    """ define rect with requirements and calc perimeter """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """  returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def area(self):
        """  return the rectangle area """
        return (self.width * self.height)

    def __str__(self):
        """ print rec in # """
        if self.width == 0 or self.height == 0:
            return ("")
        rec = []
        for i in range(self.height):
            for j in range(self.width):
                rec.append("#")
            if i != self.height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __del__(self):
        """ print messgae when deleted """
        print("Bye rectangle...")
