#!/usr/bin/python3
""" a function that writes a string to a text file (UTF8) and returns
the number of characters written"""


def write_file(filename="", text=""):
    """Prototype: def write_file(filename="", text=""):
must use the with statement
dont need to manage file permission exceptions.
function should create the file if doesnt exist.
function should overwrite the content of the file if it already exists.
not allowed to import any module"""

    with open(filename, "a", encoding="utf-8") as f:
        i = 0
        for char in text:
            f.write(char)
            i += 1
        return (i)
