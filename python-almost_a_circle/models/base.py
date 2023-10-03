#!/usr/bin/python3
"""Defines Base class"""


class Base:
    """Defines Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """On Instance initialization"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
