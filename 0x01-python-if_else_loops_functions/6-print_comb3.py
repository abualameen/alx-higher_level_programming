#!/usr/bin/python3
for g in range(10):
    for t in range(g + 1, 10):
        print("{:d}{:d}".format(g, t), end="")
        if g != 8 or t != 9:
            print(", ", end="")
print()
