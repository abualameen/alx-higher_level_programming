#!/usr/bin/python3
def remove_char_at(str, n):
    for j in range(len(str)):
        return str[:n] + str[n+1:]
