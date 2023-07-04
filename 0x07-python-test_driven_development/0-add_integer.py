#!/usr/bin/python3
# 0-add_integer
""" defines an addition function

    function that adds 2 integers
"""


def add_integer(a, b=98):
    """ adds 2 integers
    Args:
        a: int
        b:int

    Raises:
        TypeError: if a or b not a float or an int

    Returns: sum of a and b
    """

    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
