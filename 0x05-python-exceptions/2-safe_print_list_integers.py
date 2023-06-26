#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        counter = 0
        for i in my_list:
            counter += 1
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                j += 1
                if j == x:
                    break
        if counter < x:
            raise IndexError("list index out of range")
    except IndexError as e:
        print("IndexError:", str(e))
    print()
    return j

    

