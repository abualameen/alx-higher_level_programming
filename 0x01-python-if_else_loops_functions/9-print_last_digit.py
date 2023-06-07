#!/usr/bin/python3
def print_last_digit(number):
    mod = abs(number) % 10
    print(mod, end='')
    return mod
