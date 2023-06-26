#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        for i in my_list:
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                j += 1
                if j == x:
                    break
    except Exception as e:
        print("IndexError: list index out of range",str(e))
    print()
    return j

    

