#!/usr/bin/python3
"""4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Checks what an object inherits from"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
