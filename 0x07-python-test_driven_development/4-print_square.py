#!/usr/bin/python3
"""a function that prints a square with the character #.
size must be an integer, otherwise raise a TypeError
if size is less than 0, raise a ValueError
if size is a float and is less than 0, raise a TypeError"""


def print_square(size):
    """def print_square(size): prints a square with the character #
    size must be an integer
    size is not less than 0
    size is not a float"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
