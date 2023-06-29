#!/usr/bin/python3
"""
This module defines a singly linked list using
class of the object oriented programming

"""


class Node:
    """
    This clas defines a Node, with privite instaces, data and next_node

    """
    def __init__(self, data, next_node=None):
        """
        This function initializes the attributs of the
        node of a singly linked list
        Args:
            data(int): this is the data stored in the nodes
            next_node: this is like a pointer pointing to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This function retrieves the node attribute data
        Returns:

               int: the stored data in a node

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This function settes the data in a node
        to a value, and it has to be an integer, it raises various
        error if it not an integer
        Args:
            value (int): this is the value that represents the
                         data stored inthe node
        Raises:
            TypeError: if the value is not an integer

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):

        """
        this function retrievs the next_node attribute of the node class

        Returns:
            similar to a pointer to the next node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        """
        This function settes the next_node attribute of the Node class,
        it has to be a Node object other a TypeError would be raised
        Args:
            value (Node): this is the value that
                            represents the next node pointer
        Raises:
            TypeError: if the value is not a Node object

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    this class defines a singlylinkedlist

    """
    def __init__(self):
        """
        this function initiates the head of a linkedlist

        """
        self.head = None

    def sorted_insert(self, value):
        """
        this is a public defined method
        Args:
            value (int): this is the value stored

        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        this is the function that prints to the stout

        """
        if self.head is None:
            return ""
        current = self.head
        result = str(current.data) + "\n"
        while current.next_node is not None:
            current = current.next_node
            result += str(current.data) + "\n"
        return result
