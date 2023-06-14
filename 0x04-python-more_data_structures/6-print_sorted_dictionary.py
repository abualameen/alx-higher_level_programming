#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_by_keys = sorted(a_dictionary.keys())
    for key in sort_by_keys:
        print(key, ':', a_dictionary[key])
