#!/usr/bin/python3
"""
Define Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    representing a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initilize attributes

        width: width of rectangle
        Height: height of rectangle
        x: x coordinates
        y: y coordinates
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ retrieve width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieve x """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """  return the rectangle area """
        return (self.width * self.height)

    def display(self):
        """  prints in stdout the Rectangle instance with the character # """
        if self.width == 0 or self.height == 0:
            print("")
            return
        if self.y > 0:
            for o in range(0, self.y):
                print("")
        for i in range(0, self.height):
            for m in range(0, self.x):
                print(" ", end="")
            for n in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width) + "/" + str(self.height)
        return string

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute: """
        if args is not None and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    self.id = args[0]
                elif n == 1:
                    self.width = args[1]
                elif n == 2:
                    self.height = args[2]
                elif n == 3:
                    self.x = args[3]
                elif n == 4:
                    self.y = args[4]
                n += 1
            return
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
