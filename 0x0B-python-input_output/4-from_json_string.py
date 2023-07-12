#!/usr/bin/python3
"""
this module changes json format to python object

"""
import json


def from_json_string(my_str):
    """
    this function changes json format to python object

    Args:
        my_str (str): the object

    Returns:
        the python representation of json string

    """
    return json.loads(my_str)
