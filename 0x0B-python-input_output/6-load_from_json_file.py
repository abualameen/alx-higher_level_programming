#!/usr/bin/python
import json
"""
this module creates an Object from a “JSON file”:

"""


def load_from_json_file(filename):
    """
    this function creates an Object from a “JSON file”
    Args:
        filename (str): this is the file name    

    """
    with open(filename, "r") as file:
        red = file.read()
        return json.loads(red)
 
