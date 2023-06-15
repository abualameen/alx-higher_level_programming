#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_key = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del_key.append(key)
    for key in del_key:
        del a_dictionary[key]
    return a_dictionary
