#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Prototype: def read_file(filename=""):
must use the with statement
dont need to manage file permission or file doesn't exist exceptions.
are not allowed to import any module"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
