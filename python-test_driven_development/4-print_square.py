#!/usr/bin/python3
"""Module for printing a square of #"""


def print_square(size):
    """Prints a square of size size"""
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
    elif isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    else:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
