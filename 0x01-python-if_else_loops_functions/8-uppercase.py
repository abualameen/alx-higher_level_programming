#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord('A') <= ord(str[i]) <= ord('Z') or str[i] == ' ' or str[i] == '9' or str[i] == '8':
            print("{}".format(str[i]), end='')
        elif ord('a') <= ord(str[i]) <= ord('z') or str[i] == ' ':
            print("{}".format(chr(ord(str[i]) - 32)), end='')
    print()
