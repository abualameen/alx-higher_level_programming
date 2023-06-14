#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i in new:
        val = new[i] * 2
        new[i] = val
    return new
