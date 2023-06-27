#!/usr/bin/python3
# 2-square.py
""" Define square by attribute """


class Square:
    """ difine size with condition """
    def __init__(self, size=0):
        """ initialize attribute """
        try:
            if size < 0:
                raise ValueError
            self.__size = "{:d}".format(size)
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
