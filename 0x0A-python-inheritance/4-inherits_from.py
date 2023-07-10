#!/usr/bin/python3
"""
this module check if an object is an instance
of a class that inherited (directly or indirectly)
from the specified class

"""


def inherits_from(obj, a_class):
    """
    this function returns true if object
    is an instance of a class that inherited
    (directly or indirectly) from the specified class
    and False otherwise

    Args:
        obj: the object to check
        a_class: the class to check with

    Returns:
        True if an instance of a class that inherited
        (directly or indirectly) from the specified class
        and False otherwise

    """
    return isinstance(obj, a_class) and type(obj) != a_class
