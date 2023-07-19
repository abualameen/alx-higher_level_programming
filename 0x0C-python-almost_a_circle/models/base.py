#!/usr/bin/python3
"""
This module is the base class

"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this function returns a JSON string representation
        Args:
            list_dictionaries (list): the list of dictionaries
        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
