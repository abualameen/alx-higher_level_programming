#!/usr/bin/python3
"""
this module append to an exiting text

"""


def append_write(filename="", text=""):
    """
    this method appends text to an exiting text
    in a file

    Args:
        filename (str): the file name to append to
        text (str): the text to append to the file
    Returns:
        int: the number of character written

    """

    with open(filename, "a", encoding="utf-8") as file:
        num_text = file.write(text)
        return num_text
