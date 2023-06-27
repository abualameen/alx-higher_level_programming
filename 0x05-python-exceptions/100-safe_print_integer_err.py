#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise valueError("Value is not an integer")
    except Exception as e:
        print("Exception: {}".format(e), file= sys.stderr)
        return False
