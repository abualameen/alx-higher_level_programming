#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    first_key = None
    for b in a_dictionary:
        first_key = b
        break
    best_key = first_key
    best_v = a_dictionary[first_key]
    for k in a_dictionary:
        if a_dictionary[k] > best_v:
            best_key = k
            best_v = a_dictionary[k]
    return best_key
