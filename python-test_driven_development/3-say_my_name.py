#!/usr/bin/python3
"""Module for displaying name"""


def say_my_name(first_name, last_name=""):
    """Defines function for saying name"""
    first = "first_name must be a string"
    last = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(first)
    if not isinstance(last_name, str):
        raise TypeError(last)
    print("My name is {} {}".format(first_name, last_name))
