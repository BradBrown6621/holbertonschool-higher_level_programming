#!/usr/bin/python3
"""Declares a class Square"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        try:
            size * 1
            size >= 0
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")

    def area(self):
        """Defines area of a square"""
        return self.__size ** 2
