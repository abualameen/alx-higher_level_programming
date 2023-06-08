#!/usr/bin/python3
import sys
args = sys.argv[1:]
len_args = len(args)
if len_args == 1:
    print(f"{len_args} argument:")
elif len_args > 1:
    print(f"{len_args} arguments:")
else:
    print(f"{len_args} arguments.")
for h in range(len_args):
    print("{}: {}".format(h, args[h]))
