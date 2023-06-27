#!/usr/bin/python3
# 2-square.py
""" Define square by attribute """


class Square:
    """ difine size with condition """
    def __init__(self, size=0):
        """ initialize attribute """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
