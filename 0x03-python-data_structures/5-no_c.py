#!/usr/bin/python3
def no_c(my_string):
    my_str = ""
    for leta in my_string:
        if leta != 'c' and leta != 'C':
            my_str += leta
    return my_str
