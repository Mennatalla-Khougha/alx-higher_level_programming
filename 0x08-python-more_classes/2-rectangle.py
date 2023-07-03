#!/usr/bin/python3
"""
This Module contains the definition of a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle

        Args:
            width (int, optional): The width. Defaults to 0.
            height (int, optional): The height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """The perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            self.area = 0
        else:
            return 2 * (self.width + self.height)
