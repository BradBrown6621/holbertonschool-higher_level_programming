#!/usr/bin/python3
"""
Defines a square with data and methods
"""


class Square:
    """Basic Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Defines initial square params"""
        self.size(size)
        self.position(position)

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

    def position(self):
        return self.position

    def position(self, value=(0, 0)):
        """Sets the x,y tuple"""
        if (
            isinstance(value, tuple)
            and len(value) == 2
            and all(
                isinstance(element, int) 
                and element >= 0 for element in value)
            ):
            self.position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
                    if [i, j] == self.position:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("")
