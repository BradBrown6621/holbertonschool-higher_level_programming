#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
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

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
