#!/usr/bin/python3
"""
this module adds all arguments to a Python list, and then save them to a file

"""
import sys
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def args_add_to_list(args: List[str]):
    """
    this functon adds all arguments to a Python
    list, and then save them to a file
    Args:
        args: the areguments

    """
    filename = "add_item.json"
    try:
        existing_list = load_from_json_file(filename)
    except FileNotFoundError:
        existing_list = []
    new_list = existing_list + args
    save_to_json_file(new_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    args_add_to_list(args)
