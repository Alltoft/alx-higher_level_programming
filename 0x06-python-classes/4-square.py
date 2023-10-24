#!/usr/bin/python3
'''a class Square that defines a square by size and area
with property'''


class Square:
    '''defining sizes and area with handleing the errors
    with property'''
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        self.Sarea = self.__size * self.__size
        return self.Sarea
