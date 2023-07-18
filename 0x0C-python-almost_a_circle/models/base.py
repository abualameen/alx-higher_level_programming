#!/usr/bin/python3
"""
This module is the base class

"""


class Base:
    """
    This is the Base

    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        this function instantiate the base base instance
        
        Args:
            id (int): the id presented as an argument

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

