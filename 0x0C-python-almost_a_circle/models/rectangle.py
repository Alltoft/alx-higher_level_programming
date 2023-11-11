#!/usr/bin/python3
"""a Rectangle class that inherits from the class Base"""
from models.base import Base


class Rectangle (Base):

    """defining the class attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
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

    """the width attribute getter"""
    @property
    def width(self):
        return self.__width

    """the width attribute setter"""
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    """the height attribute getter"""
    @property
    def height(self):
        return self.__height

    """the height attribute setter"""
    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")

        self.__height = h

    """the x attribute getter"""
    @property
    def x(self):
        return self.__x

    """the x attribute setter"""
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """the y attribute getter"""
    @property
    def y(self):
        return self.__y

    """the y attribute setter"""
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """a public method  that returns the area value of
    the Rectangle instance"""
    def area(self):
        return self.__height * self.width

    """a public method that prints in stdout
    the Rectangle instance with the character #
    by taking care of x and y"""
    def display(self):
        for p in range(self.__y):
            print()
        for i in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    """the __str__ method so that it returns
    [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
    def __str__(self):
        new_str = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"
        return new_str

    """a public method that assigns an argument to each attribute
    or assigns a key/value argument to attributes"""
    def update(self, *args, **kwargs):
        attrs = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if arg is not None:
                setattr(self, attrs[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    """a public method  that returns
    the dictionary representation of a Rectangle"""
    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
