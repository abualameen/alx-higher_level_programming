#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_new = []
    try:
        for k in range(list_length):
            try:
                result = my_list_1[k] / my_list_2[k]
            except ZeroDivisionError:
                result = 0
                print("division by o")
            except TypeError:
                result = 0
                print("wrong type")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                list_new.append(result)
    finally:
        return list_new
