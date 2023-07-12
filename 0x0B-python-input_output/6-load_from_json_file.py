#!/usr/bin/python
"""
this module creates an Object from a “JSON file”:

"""
import json


def load_from_json_file(filename):
    """
    this function creates an Object from a “JSON file”
    Args:
        filename (str): this is the file name    

    """
    with open(filename, "r") as file:
        lod = json.load(file)
        return lod
 
