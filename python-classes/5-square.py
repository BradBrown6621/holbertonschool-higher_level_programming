#!/usr/bin/python3
"""
Defines a square with data and methods
"""


class Square:
    """Basic Square"""
    def __init__(self, size=0):
        """Defines initial square params"""
        self.size(size)

    def size(self):
        """Returns the size of Square"""
        return self.size

    def size(self, value):
        """Sets the size of square"""
        if isinstance(value, int):
            if value >= 0:
                self.size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of a square"""
        try:
            if self.size >= 0:
                return self.size ** 2
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Prints a square"""
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print("")
