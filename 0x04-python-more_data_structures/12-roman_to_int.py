#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    solution = 0
    prev_val = 0
    for ele in roman_string:
        if ele in dict_roman:
            val = dict_roman[ele]
            if val > prev_val:
                solution += val - 2 * prev_val
            else:
                solution += val
            prev_val = val
        else:
            return 0
    return solution
