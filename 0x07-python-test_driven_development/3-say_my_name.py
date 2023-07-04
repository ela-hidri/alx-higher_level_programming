#!/usr/bin/python3
"""
Defines a function that prints Full name

Attributes:
    say_my_name: prints Fullname
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>

    Args:
    first_name: first name
    last_name: last name

    Raises:
    TypeError: first_name must be a string
    TypeError: last_name must be a string

    Returns: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
