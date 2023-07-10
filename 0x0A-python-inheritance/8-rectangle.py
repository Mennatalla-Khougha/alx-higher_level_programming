#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This modula is a subclass of BaseGeometry"""


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
