#!/usr/bin/python3
"""a function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """Prototype: def from_json_string(my_str):
dont need to manage exceptions if the JSON string
doesnt represent an object."""

    return (json.loads(my_str))
