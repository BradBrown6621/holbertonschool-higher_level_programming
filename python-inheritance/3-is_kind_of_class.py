#!/usr/bin/python3
"""3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
