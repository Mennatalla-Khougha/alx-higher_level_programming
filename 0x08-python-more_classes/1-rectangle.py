#!/usr/bin/python3
"""
This Module contains the definition of a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """This function initializes the rectangle

        Args:
            width (int, optional): Defaults to 0.
            height (int, optional): Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle

        Returns:
            int: the width of the rectangle
        """
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Returns the height of the rectangle

        Returns:
            int: the height of the rectangle
        """
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

