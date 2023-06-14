#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for ele in set_1:
        if ele not in set_2:
            new.append(ele)
    for ele in set_2:
        if ele not in set_1:
            new.append(ele)
    return new
