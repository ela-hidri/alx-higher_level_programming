#!/usr/bin/python3
# 2-rectangle.py
""" defines a rectangle """


class Rectangle():
    """ define rect with requirements and calc perimeter """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieve width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """  returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def area(self):
        """  return the rectangle area """
        return (self.width * self.height)

    def __str__(self):
        """ print rec in # """
        if self.width == 0 or self.height == 0:
            return ("")
        rec = []
        for i in range(self.height):
            for j in range(self.width):
                rec.append(str(self.print_symbol))
            if i != self.height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """ return a string representation """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ print messgae when deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ turns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return (rect_1)
        elif rect_1.area() < rect_2.area():
            return rect_2
