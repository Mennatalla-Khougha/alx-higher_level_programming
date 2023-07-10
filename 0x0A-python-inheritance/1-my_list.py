#!/usr/bin/python3
"""This modula sort the elements of a list"""


class MyList(list):
    """This class define a subclass that print a sorted list

    Args:
        list (list): list to sorted
    """
    def __init__(self, *args):
        """initialize the class
        """
        super().__init__(*args)

    def print_sorted(self):
        """print a sorted list
        """
        sort_list = sorted(self)
        print(sort_list)
