#!/usr/bin/python3
'''a class Square that defines a square by size and area
with property'''


class Square:
    '''defining sizes and area with handleing
    the errors with property'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position[0] = value[0]
        self.__position[1] = value[1]

    def area(self):
        self.Sarea = self.__size * self.__size
        return self.Sarea

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for nl in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for sp in range(self.__position[0]):
                    print(" ", end="")
                for a in range(self.__size):
                    if self.__size != 0:
                        print("#", end="")
                    else:
                        print()
                print()
