#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    add = 0
    for j in range(len(args)):
        add = int(args[j]) + add
    print("{}".format(add))
