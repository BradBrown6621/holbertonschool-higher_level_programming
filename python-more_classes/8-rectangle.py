#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle():
    """A definition of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
        def bigger_or_equal(rect_1, rect_2):
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2

    def __init__(self, width=0, height=0):
        """Initializes instance of Rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets Rectangle.width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets Rectangle.width to int"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets Rectangle.height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets Rectangle.height to int"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns string representation of Rectangle instance"""
        if self.width == 0 or self.height == 0:
            return ""

        string = ""
        for i in range(self.height):
            string = string + str(self.print_symbol) * self.width + "\n"

        return string[:-1]

    def __repr__(self):
        """
        Returns a string representation of Rectangle used by eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Performs functions when deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
