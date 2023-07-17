#!/usr/bin/python3
""" Define Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    representing a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initilize attributes

        size: height of square
        x: x coordinates
        y: y coordinates
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        self.width = value
        self.height = value

    def __str__(self):
        """
        [print] (<id>) <x>/<y> - <size>
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.size) 
        return string
