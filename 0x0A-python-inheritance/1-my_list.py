#!/usr/bin/python3
"""
This module is a class that inherites from another class

"""


class MyList(list):
    """
    this class inherites from list and has a method print_sorted

    Public Methods:
    - print_sorted(): this prints the list sorted in ascending order.

    """

    def print_sorted(self):
        """
        this prints the list sorted in ascending order.

        """
        if len(self) == 0:
            print([])
        elif all(isinstance(ele, int) for ele in self):
            list_sorted = sorted(self)
            print(list_sorted)
        else:
            print("Error: non-integer elements in the List")
