#!/usr/bin/python3
"""
define a class that inheerits from int
"""


class MyInt(int):
    """
    rebel
    """
    def __eq__(self, value):
        """ invert """
        return (self.real != value)
    
    def __ne__(self, value):
        """ invert """
        return (self.real == value)
