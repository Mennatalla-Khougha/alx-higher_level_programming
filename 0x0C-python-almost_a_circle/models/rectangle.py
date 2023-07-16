#!/usr/bin/python3
"""This module define the class rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Define a class Rectangle that inherits from Base

    Args:
        Base (Class): The base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle class

        Args:
            width (int): The width
            height (int): The height
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set the x property"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set the y property"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Define the area of the Rectangle

        Returns:
            int: Rectangle area
        """
        return self.__height * self.__width

    def display(self):
        """Display the Rectangle to the stdout"""
        for k in range(self.y):
            print('')
        for i in range(self.height):
            for n in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        """Define the string representation of the Rectangle
        
        Returns:
            str: string representation of the Rectangle
        """
        msg = '[Rectangle] (' + str(self.id) + ') ' + str(self.x) + '/' + str(self.y)
        msg += ' - ' + str(self.width) + '/' + str(self.height)
        return msg

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: Variable-length argument list.
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            *kwargs: key - value pair of args
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
