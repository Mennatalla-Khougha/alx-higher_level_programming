#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This modula is a subclass of BaseGeometry"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
