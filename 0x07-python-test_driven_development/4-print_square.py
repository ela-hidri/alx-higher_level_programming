#!/usr/bin/python3
# 4-print_square
""" defines a function that prints a square

Attributes:
    print_square: prints sqaure
"""


def print_square(size):
    """
    prints a square with the character #.

    Args:
    size: size of square

    Raises:
    TypeError: if size not int
    ValueError: if size < 0
    TypeError: if size is a float and less than 0

    Return: nothing
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for n in range(size):
            print("#", end="")
        print("")
