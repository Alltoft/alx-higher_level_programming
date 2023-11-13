#!/usr/bin/python3
"""a class Base that refer to the base class of other classes"""
import json


class Base:
    """A base class for other classes in the project"""


    __nb_objects = 0

    def __init__(self, id=None):
        """defining the class attributes"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns the JSON string representation of
        list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that writes the JSON string
        representation of list_objs to a file"""
        conv = []
        for i in list_objs:
            conv.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(conv))

    @staticmethod
    def from_json_string(json_string):
        """a static method that returns the list of the
        JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """a  class method that returns an instance
        with all attributes already set (using a "dummy")"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """a class method that returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                file_data = f.read()
                if not file_data:
                    return []
                js_list = cls.from_json_string(file_data)
                ret_list = []
                for i in js_list:
                    ret_list.append(cls.create(**i))
                return ret_list
        except FileNotFoundError:
            return []
