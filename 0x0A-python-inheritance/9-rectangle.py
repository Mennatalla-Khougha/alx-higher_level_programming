#!/usr/bin/python3
"""This modula is a subclass of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a subclass

    Args:
        BaseGeometry (class): Baseclass
    """
    def __init__(self, width, height):
        """initialize the class

        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        msg = "[Rectangle] " + str(self.__width) + '/' + str(self.__height)
        return msg
