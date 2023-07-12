#!/usr/bin/python3
import json
"""
this module has a function that write a object to a file using
JSON representation

"""


def save_to_json_file(my_obj, filename):
    """
    this function write a object to a file using JSON representation
    Args:
        my_obj (str): this is the obj
        filename (str): this is the file name

    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
