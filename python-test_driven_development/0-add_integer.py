#!/usr/bin/python3
"""Module adds 2 integers"""


def add_integer(a, b=98):
    """Adds 2 integers and returns the result"""
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
