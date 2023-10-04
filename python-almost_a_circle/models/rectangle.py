#!/usr/bin/python3
"""models/rectangle.py"""


from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for instances of Rectangles"""
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
        """Width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width to a natural number"""
        self.validate_natural_nums(width, 'width')
        self.__width = width

    @property
    def height(self):
        """Height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height to a natural number"""
        self.validate_natural_nums(height, 'height')
        self.__height = height

    @property
    def x(self):
        """x-axis of Rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x property to a whole number"""
        self.validate_whole_nums(x, 'x')
        self.__x = x

    @property
    def y(self):
        """y-axis of Rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y property to a whole number"""
        self.validate_whole_nums(y, 'y')
        self.__y = y

    def area(self):
        """
        Returns the area of the Rectangle
        """
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
        """String representation of Rectangle"""
        return "{} ({}) {}/{} - {}/{}".format(
                "Rectangle",
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args):
        """Updates Rectangle using new values"""
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except Exception:
            pass

    def validate_ints(self, value, value_name):
        """Raises errors if value isn't an int"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(value_name))

    def validate_natural_nums(self, value, value_name):
        """Raises error if value isn't greater than 0"""
        self.validate_ints(value, value_name)
        if value <= 0:
            raise ValueError("{} must be > 0".format(value_name))

    def validate_whole_nums(self, value, value_name):
        """Raises errors if value is a negative number"""
        self.validate_ints(value, value_name)
        if value < 0:
            raise ValueError("{} must be >= 0".format(value_name))
