#!/usr/bin/python3
"""
this model find the peak

"""

def find_peak(list_of_integers):
    """ this function  """
    center_idx = len(list_of_integers) // 2
    current_ele = list_of_integers[center_idx]

    if (center_idx == 0 or current_ele >= list_of_integers[center_idx - 1]) and \
       (center_idx == len(list_of_integers) - 1 or current_ele >= list_of_integers[center_idx + 1]):
        # If the current element is greater than or equal to its neighbors or at the boundary,
        # it's a peak.
        peak = current_ele
    else:
        if center_idx > 0 and current_ele < list_of_integers[center_idx - 1]:
            # If the current element is smaller than its left neighbor, go left.
            peak = find_peak(list_of_integers[:center_idx])
        else:
            # Otherwise, go right.
            peak = find_peak(list_of_integers[center_idx + 1:])
    
    return peak

