#!/usr/bin/python3
import json
"""a function that returns the JSON
representation of an object (string)"""


def to_json_string(my_obj):
    """Prototype: def to_json_string(my_obj):
dont need to manage exceptions if the object cant be serialized."""

    return (json.dumps(my_obj))