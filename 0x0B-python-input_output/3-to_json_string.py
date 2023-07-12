#!/usr/bin/python3
"""
this module returns json representation of an object in string

"""
import json


def to_json_string(my_obj):
    """
    this function returns the json representation of an object
    Args:
        my_obj (str): the object

    Returns:
        the json representation of the object

    """
    return json.dumps(my_obj)
