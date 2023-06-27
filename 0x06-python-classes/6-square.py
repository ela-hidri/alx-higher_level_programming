#!/usr/bin/python3
# 6-square.py
""" Define Square """


class Square:
    """define size with condition and calc area """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize attribute """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ get position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set position """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return square area """
        return (self.size * self.size)

    def my_print(self):
        """ print square """
        if self.size == 0:
            print("")
            return
        if self.position[1] > 0:
            for i in range(0, self.position[1]):
                print("")
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for n in range(self.size):
                print("#", end="")
            print("")
