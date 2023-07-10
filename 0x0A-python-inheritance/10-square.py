#!/usr/bin/python3
"""
define a class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    nherits from BaseGeometry
    """

    def __init__(self, size):
        """
        initialise var

        Args:
            self: class
            size: size of Square
        Return:
            nothing
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
