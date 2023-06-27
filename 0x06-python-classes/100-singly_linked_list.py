#!/usr/bin/python3
"""Define a singly linked list"""


class Node:
    """A class Node Define a node of singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Initialize node of singly linked list

        Args:
            data (int): The data of the node
            next_node (node): pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Access the data property"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Access the next node property"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A class that define a singly linked list"""

    def __init__(self):
        """Initialize the singly linked list"""
        self.head = None

    def sorted_insert(self, value):
        """insert a new node to the singly linked list

        Args:
            value (node): the node to insert
        """
        current = Node(value)
        if self.head is None:
            current.next_node = None
            self.head = current
        elif self.head.data > value:
            current.next_node = self.head
            self.head = current
        else:
            tmp = self.head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            current.next_node = tmp.next_node
            tmp.next_node = current

    def __str__(self):
        """Return a string representation of the singly linked list"""
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
