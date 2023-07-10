#!/usr/bin/python3
"""
This module returns True if a object is exactly an
instance a the specified class otherwise False

"""


def is_same_class(obj, a_class):
    """
    this function checks if an object is exactly an
    instance a the specified class otherwise False

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
