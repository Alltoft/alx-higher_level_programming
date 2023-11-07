#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Prototype: def load_from_json_file(filename):
You must use the with statement
You dont need to manage exceptions if the JSON string doesnt
represent an object.
You dont need to manage file permissions / exceptions."""

    with open(filename, "r") as f:
        return (json.load(f))
