#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        return "{} ({}) {}/{} - {}".format(
                "Square",
                self.id,
                self.x,
                self.y,
                self.__size
                )

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, width):
        Rectangle.validate_natural_nums(self, width, "width")
        self.__width = width
        self.__height = width
        self.__size = width

    def update(self, *args, **kwargs):
        if len(args) > 0:
            try:
                self.id = args[0]
                self.__size = args[1]
                Rectangle.x = args[2]
                Rectangle.y = args[3]
            except Exception:
                pass
        else:
            for key, item in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, item)
