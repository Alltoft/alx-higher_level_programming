#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
Private instance attribute: width
Private instance attribute: height
counting the perimiter and the area
prints the rectangle with the character initialized to print_symbol
return a string representation of the rectangle
with handling when an instance of Rectangle is deleted
Incremented or Decremented during each new instance instantiation \
    or deletion"""


class Rectangle:
    """Instantiation with optional width and height:
    def __init__(self, width=0, height=0)
    returns the rectangle area
    returns the rectangle perimeter
    printing the rectangle with the character initialized to print_symbol
    returning a string representation of the rectangle
    handling here when an instance of Rectangle is deleted"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        new_str = ""
        for i in range(self.__height - 1):
            new_str += str(self.print_symbol) * self.__width + "\n"
        new_str += str(self.print_symbol) * self.__width
        return new_str

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + \
            str(self.__height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")