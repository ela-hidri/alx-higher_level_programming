#!/usr/bin/python3
# 3-square.py
""" Define Square """


class Square:
    """define size with condition and calc area """
    def __init__(self, size):
        """ initialize attribute """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return square area """
        return (self.__size * self.__size)
