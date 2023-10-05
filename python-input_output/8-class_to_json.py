#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
    """Returns a dictionary representation of obj"""
    return obj.__dict__
