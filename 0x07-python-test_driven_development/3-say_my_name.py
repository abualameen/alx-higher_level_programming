#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name is None and last_name is None:
        raise TypeError("first_name cant be None")
    elif first_name == None:
        raise TypeError("first_name must be a string")
    if not first_name and not last_name:
        raise TypeError("first_name cant be empty")
    print("My name is {} {}".format(first_name, last_name))
