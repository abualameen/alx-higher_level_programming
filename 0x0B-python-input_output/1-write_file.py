#!/usr/bin/python3
"""
this module is a python write module for writing into a file

"""


def write_file(filename="", text=""):
    """
    this function writes text into the file
    Args:
        filename (str): the file name to open
        text (str): the text to write to the file
    Raises:
        FileNotFoundError: if the specified file doesn't exist
    Returns:
        int: Number of character written

    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return file.tell()
