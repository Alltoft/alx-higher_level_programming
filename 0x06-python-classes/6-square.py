#!/usr/bin/python3
'''calc square'''


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position"""

        self.size = size

        self.position = position

    @property
    def size(self):
        """Return the size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Return the position attribute"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position attribute"""

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current square area"""

        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters and position"""

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
