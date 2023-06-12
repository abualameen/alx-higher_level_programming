#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list1 = []
    if idx < 0:
        my_list1 = my_list
        return my_list1
    elif idx >= len(my_list):
        my_list1 = my_list
        return my_list1
    for i in range(len(my_list)):
        my_list1.append(my_list[i])
    my_list1[idx] = element
    return my_list1
