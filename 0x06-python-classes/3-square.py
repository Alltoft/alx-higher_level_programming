#!/usr/bin/python3
'''a class Square that defines a square by size and area'''


class Square:
    '''defining sizes and area with handleing the errors'''
    def __init__(self, size=0):
        if (int(size) < 0):
            raise ValueError("size must be >= 0")
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")

        self.__size = size

    def area(self):
        self.Sarea = self.__size * self.__size
        return self.Sarea
