#!/usr/bin/python3
"""
This module has a function that returns all attributes and methods of an object

"""
def lookup(obj):
    """
    this function returns the list of available attributes and methods of an object.

    """
    return list(dir(obj))
