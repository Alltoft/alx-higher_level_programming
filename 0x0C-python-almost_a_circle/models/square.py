#!/usr/bin/python3
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        attrs = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            if arg is not None:
                setattr(self, attrs[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)
    def to_dictionary(self):
        return {
            'id' : self.id,
            'x' : self.x,
            'size' : self.size,
            'y' : self.y
            }
