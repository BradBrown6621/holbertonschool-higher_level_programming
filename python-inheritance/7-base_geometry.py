#!/usr/bin/python3
"""5-base_geometry.py"""


class BaseGeometry:
    """Base class for all shapes EVER"""

    def area(self):
        """Returns area to outside code"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks that inputs passed are integers (specifically natural numbers)
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
