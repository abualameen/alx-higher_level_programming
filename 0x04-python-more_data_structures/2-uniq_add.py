#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list1 = []
    add_all = 0
    for ele in my_list:
        if ele not in my_list1:
            my_list1.append(ele)
    for ele in my_list1:
        add_all += ele
    return add_all
