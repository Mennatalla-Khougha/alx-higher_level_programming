#!/usr/bin/python3
"""This modula is a subclass of int"""


class MyInt(int):
    """This is a subclass of int"""
    def __eq__(self, other):
        """Reverse the equal function

        Args:
            other (int): number to be compared against

        Returns:
            Bool: True or False
        """
        return self.real != other

    def __ne__(self, other):
        """Reverse the not equal function

        Args:
            other (int): number to be compared against

        Returns:
            Bool: True or False
        """
        return self.real == other
