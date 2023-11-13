#!/usr/bin/python3
"""a Rectangle class that inherits from the class Base"""
from models.base import Base


class Rectangle (Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """defining the class attributes"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """the width attribute getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """the width attribute setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """the height attribute getter"""
        return self.__height

    @height.setter
    def height(self, h):
        """the height attribute setter"""
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")

        self.__height = h

    @property
    def x(self):
        """the x attribute getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """the x attribute setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """the y attribute getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """the y attribute setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """a public method  that returns the area value of
        the Rectangle instance"""
        return self.__height * self.width

    def display(self):
        """a public method that prints in stdout
        the Rectangle instance with the character #
        by taking care of x and y"""
        for p in range(self.__y):
            print()
        for i in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        new_str = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"
        return new_str

    def update(self, *args, **kwargs):
        """a public method that assigns an argument to each attribute
        or assigns a key/value argument to attributes"""
        attrs = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if arg is not None:
                setattr(self, attrs[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """a public method  that returns
        the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
