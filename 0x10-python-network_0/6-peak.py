#!/usr/bin/python3

"""
this model find the peak of a list

"""


def find_peak(list_of_integers):
    """ find the peak """
    center_idx = len(list_of_integers) // 2
    current_ele = list_of_integers[center_idx]

    if (
        (center_idx == 0 or current_ele >=
            list_of_integers[center_idx - 1]) and
        (center_idx == len(list_of_integers) - 1
            or current_ele >= list_of_integers[center_idx + 1])
    ):
        peak = current_ele
    else:
        if center_idx > 0 and current_ele < list_of_integers[center_idx - 1]:
            peak = find_peak(list_of_integers[:center_idx])
        else:
            # Otherwise, go right.
            peak = find_peak(list_of_integers[center_idx + 1:])
    return peak
