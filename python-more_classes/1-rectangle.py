#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle():
    """A definition of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes instance of Rectangle"""
        self.__width = width
        self.__height = height

    def width(self):
        """Gets Rectangle.width"""
        return self.__width

    def width(self, value):
        """Sets Rectangle.width to int"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def height(self):
        """Gets Rectangle.height"""
        return self.__height

    def height(self, value):
        """Sets Rectangle.height to int"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
