#!/usr/bin/python3
"""
define function that returns list
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object:
    """
    return dir(obj)
