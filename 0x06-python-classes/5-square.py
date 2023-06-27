#!/usr/bin/python3
# 5-square.py
""" Define Square """


class Square:
    """define size with condition and calc area """
    def __init__(self, size=0):
        """ initialize attribute """
        self.size = size

    @property
    def size(self):
        """ get size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set Size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return square area """
        return (self.size * self.size)

    def my_print(self):
        """ print square """
        if self.size == 0:
            print("")
        for i in range(self.size):
            for n in range(self.size):
                print("#", end="")
            print("")
