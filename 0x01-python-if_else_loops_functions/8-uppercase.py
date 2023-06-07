#!/usr/bin/python3
def uppercase(str):
    strr = ""
    for i in range(len(str)):
        if (ord('A') <= ord(str[i]) <= ord('Z') or
                str[i] == ' ' or '0' <= str[i] <= '9' or str[i] == ','):
            strr += str[i]
        elif ord('a') <= ord(str[i]) <= ord('z'):
            strr += chr(ord(str[i]) - 32)
    print("{}".format(strr), end='')
    print()
