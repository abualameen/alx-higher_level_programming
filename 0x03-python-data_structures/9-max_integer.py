#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    gtest = my_list[0]
    for ele in my_list:
        if ele > gtest:
            gtest = ele
        else:
            gtest = gtest
    return gtest
