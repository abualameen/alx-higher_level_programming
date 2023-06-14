#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list1 = []
    for i in range(len(my_list)):
        my_list1.append(my_list[i])
    for j in range(len(my_list1)):
        if my_list1[j] == search:
            my_list1[j] = replace
    return my_list1
