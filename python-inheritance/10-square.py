#!/usr/bin/python3
"""10-square.py"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Defines a Square"""

    def __init__(self, size):
        """Run when instance is created of Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of Square"""
        return self.__size ** 2
