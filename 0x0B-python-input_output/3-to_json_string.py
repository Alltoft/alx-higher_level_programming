#!/usr/bin/python3
"""a function that returns the JSON
representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Prototype: def to_json_string(my_obj):
dont need to manage exceptions if the object cant be serialized."""

    return (json.dumps(my_obj))
