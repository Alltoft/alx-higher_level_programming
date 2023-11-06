#!/usr/bin/python3
"""a class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """def area(self): that raises an Exception with
    the message area() is not implemented"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
