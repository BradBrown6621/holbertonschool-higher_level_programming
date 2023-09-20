#!/usr/bin/python3
"""Declares a class Square"""


class Square:
    """Square with error handling"""
    def __init__(self, size=0):
        """On initialization"""
        try:
            size * 1
            size >= 0
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
