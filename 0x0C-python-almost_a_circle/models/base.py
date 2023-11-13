#!/usr/bin/python3
"""a class Base that refer to the base class of other classes"""
import json


# class Base:
#     __nb_objects = 0

#     """defining the class attributes"""
#     def __init__(self, id=None):
#         if id:
#             self.id = id
#         else:
#             Base.__nb_objects += 1
#             self.id = Base.__nb_objects

#     """a static method that returns the JSON string representation of
#     list_dictionaries"""
#     @staticmethod
#     def to_json_string(list_dictionaries):
#         if not list_dictionaries:
#             return "[]"
#         return json.dumps(list_dictionaries)

#     """a class method that writes the JSON string
#     representation of list_objs to a file"""
#     @classmethod
#     def save_to_file(cls, list_objs):
#         conv = []
#         for i in list_objs:
#             conv.append(cls.to_dictionary(i))
#         with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
#             f.write(cls.to_json_string(conv))

#     """a static method that returns the list of the
#     JSON string representation json_string"""
#     @staticmethod
#     def from_json_string(json_string):
#         if not json_string:
#             return []
#         return json.loads(json_string)

#     """a  class method that returns an instance
#     with all attributes already set (using a "dummy")"""
#     @classmethod
#     def create(cls, **dictionary):
#         dummy = cls(1, 1)
#         dummy.update(**dictionary)
#         return dummy

#     """a class method that returns a list of instances"""
#     @classmethod
#     def load_from_file(cls):
#         try:
#             with open(cls.__name__ + ".json", "r") as f:
#                 file_data = f.read()
#                 if not file_data:
#                     return []
#                 js_list = cls.from_json_string(file_data)
#                 ret_list = []
#                 for i in js_list:
#                     ret_list.append(cls.create(**i))
#                 return ret_list
#         except FileNotFoundError:
#             return []

class Base:
    """A base class for other classes in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor
        Args:
            id (int, optional): The id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries
        Returns:
            str: The JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"  # Return an empty string if list_dictionaries is None
        else:
            # Return the JSON string using json.dumps
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"

        list_dicts = []
        if list_objs is not None:

            for obj in list_objs:

                list_dicts.append(obj.to_dictionary())
        with open(filename, "w") as f:

            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str): A string representing a list of dictionaries

        Returns:
            list: The list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:

            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary (dict): A dictionary of attributes and values
        Returns:
            Base: An instance of Base or its subclasses
        """
        if cls.__name__ == "Rectangle":

            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        Returns:
            list: A list of instances of Base or its subclasses
        """

        filename = cls.__name__ + ".json"
        list_instances = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
            for dict in list_dicts:

                list_instances.append(cls.create(**dict))
        return list_instances
