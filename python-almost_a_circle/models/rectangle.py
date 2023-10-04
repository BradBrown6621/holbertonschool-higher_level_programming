#!/usr/bin/python3
"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.validate_natural_nums(width, "width")
        self.__width = width

        self.validate_natural_nums(height, "height")
        self.__height = height

        self.validate_whole_nums(x, "x")
        self.__x = x

        self.validate_whole_nums(y, "y")
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.validate_natural_nums(width, 'width')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.validate_natural_nums(height, 'height')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.validate_whole_nums(x, 'x')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validate_whole_nums(y, 'y')
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        """Prints self using # for each cell"""
        for y in range(0, self.y):
            print("")
        for i in range(0, self.height):
            for x in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        return "{} ({}) {}/{} - {}/{}".format(
                "Rectangle",
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args):
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except Exception:
            pass

    def validate_ints(self, value, value_name):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(value_name))

    def validate_natural_nums(self, value, value_name):
        self.validate_ints(value, value_name)
        if value <= 0:
            raise ValueError("{} must be > 0".format(value_name))

    def validate_whole_nums(self, value, value_name):
        self.validate_ints(value, value_name)
        if value < 0:
            raise ValueError("{} must be >= 0".format(value_name))
