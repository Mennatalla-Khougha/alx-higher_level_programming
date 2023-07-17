#!/usr/bin/python3
"""This module define the class square that inherit from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class define the square class
    Args:
        Rectangle(class): class to inherit from
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square class

        Args:
            size (int): size
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size property"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square class

        Returns:
            str: string representation
        """
        msg = '[Square] (' + str(self.id) + ') '
        msg += str(self.x) + '/' + str(self.y)
        msg += ' - ' + str(self.width)
        return msg

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
