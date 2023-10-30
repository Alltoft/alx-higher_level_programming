#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
Private instance attribute: width
Private instance attribute: height
counting the perimiter and the area"""


class Rectangle:
    """Instantiation with optional width and height:
    def __init__(self, width=0, height=0)
    returns the rectangle area
    returns the rectangle perimeter"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        self.rec_area = self.__height * self.__width
        return self.rec_area

    def perimeter(self):
        self.rec_per = 0
        self.rec_per = (self.__height + self.__width) * 2
        return self.rec_per
