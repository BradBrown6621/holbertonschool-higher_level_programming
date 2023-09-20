#!/usr/bin/python3
class Square:
    """Basic Square"""
    def __init__(self, size=0):
        """Defines initial square params"""
        self.size(size)

    def size(self):
        return self.size

    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        try:
            if self.size >= 0:
                return self.size ** 2
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
