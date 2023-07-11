#!/usr/bin/python3
def read_file(filename=""):
    """
    This functio Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.

    Raises:
        FileNotFoundError: If the specified file doesn't exist.

    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
             print(line, end="")
