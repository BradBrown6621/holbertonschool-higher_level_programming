#!/usr/bin/python3
"""Defines Base class"""

import json
import os

class Base:
    """Defines Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """On Instance initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        save = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                save.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(save))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = cls()

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        list_instances = []
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                list_dicts = cls.from_json_string(file.read())

            for dict_obj in list_dicts:
                list_instances.append(cls.create(**dict_obj))
        return list_instances
