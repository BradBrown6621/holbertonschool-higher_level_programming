#!/usr/bin/python3
"""8-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class definition of Rectangles"""

    def __init__(self, width, height):
        """Called when instance is created"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of Rectangle"""
        return "[{}] {}/{}".format(
                "Rectangle",
                self.__width,
                self.__height)
