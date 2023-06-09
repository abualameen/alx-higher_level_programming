#!/usr/bin/python3
def magic_calculation(a, b):
    if __name__ == "__main__":
        add, sub = __import__('magic_calculation_102', list=('add', 'sub'))
        if a < b:
            c = add(a, b)
            for i in range(4, 6):
                c = add(c, i)
            return c
        else:
            return sub(a, b)
