#!/usr/bin/python3
"""
this module returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:

"""


def class_to_json(obj):
    """
    this function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
    Args:
        obj (str): the object

    """

    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return {}
