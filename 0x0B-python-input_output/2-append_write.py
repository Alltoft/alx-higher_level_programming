#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """Prototype: def append_write(filename="", text=""):
If the file doesnt exist, it should be created
must use the with statement
dont need to manage file permission or file doesn't exist exceptions.
not allowed to import any module"""

    with open(filename, "a", encoding="utf-8") as f:
        i = 0
        for char in text:
            f.write(char)
            i += 1
        return (i)
