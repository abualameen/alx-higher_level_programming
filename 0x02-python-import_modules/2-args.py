#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    len_args = len(args)
    if len_args == 1:
        print("1 argument:")
    elif len_args == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len_args))
    for h in range(len_args):
        print("{}: {}".format(h+1, args[h]))
