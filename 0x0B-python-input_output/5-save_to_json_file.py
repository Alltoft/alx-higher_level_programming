#!/usr/bin/python3
"""a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """must use the with statement
dont need to manage exceptions if the object cant be serialized.
dont need to manage file permission exceptions."""

    with open(filename, "w") as f:
        return (json.dump(my_obj, f))
