#!/usr/bin/python3
"""This Module prevent the user from creating new instances attributes"""


class LockedClass:
    """Define a Locked class
    """
    __slots__ = ('first_name', )

    def setattr(self, name, value):
        """Define the attribute

        Args:
            name (str): first_name
            value (str): first_name
        """
        if name == 'first_name':
            self.__dict__[name] = value
