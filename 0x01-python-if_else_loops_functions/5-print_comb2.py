#!/usr/bin/python3
for g in range(0, 100):
    if g != 99:
        print("{:02d}".format(g), end=', ')
    if g == 99:
        print("{}".format(g))
