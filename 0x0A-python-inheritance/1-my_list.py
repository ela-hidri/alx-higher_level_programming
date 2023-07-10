#!/usr/bin/python3
"""
define a class that inheerits
"""


class MyList(list):
    """
    inherites from list and print list sorted
    """
    def print_sorted(self):
        print(sorted(self))
