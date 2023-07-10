#!/usr/bin/python3
"""
This module returns True if a object is exactly an
instance a the specified class otherwise False

"""


def is_same_class(obj, a_class):
    """
    this function checks if an object is exactly an
    instance a the specified class otherwise False

    Args:
       obj: An object to check on.
       a_class: A class to compare with
    
    Returns:
        True if the object is exactly an instance of the class;
        False otherwise.

    """
    return type(obj) is a_class
