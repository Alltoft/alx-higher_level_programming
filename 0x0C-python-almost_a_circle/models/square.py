#!/usr/bin/python3
"""a Square class that inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """defining the attributes of the Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """the size attribute getter"""
    @property
    def size(self):
        return self.width

    """the size attribute setter"""
    @size.setter
    def size(self, size):
        self.width = size

    """The overloading __str__ method should return
    [Square] (<id>) <x>/<y> - <size>"""
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    """a public method that assigns attributes"""
    def update(self, *args, **kwargs):
        attrs = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            if arg is not None:
                setattr(self, attrs[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    """a public method that returns
    the dictionary representation of a Square """
    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
            }
