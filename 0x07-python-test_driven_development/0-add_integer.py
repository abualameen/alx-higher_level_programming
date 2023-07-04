#!/usr/bin/python3
"""
this is a add module it works in cojection
with the 0-main.py 

"""
def add_integer(a, b=98):
    """
    Returns a * b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a is None and b is None:
        raise TypeError("Both a and b cant be None")
    elif a is None:
        raise TypeError("a must be an integer")
    if not a and not b:
        raise ValueError("Both a and b cant be empty")
    elif not a:
        raise ValueError("a cant be empty")
    a = int(a)
    b = int(b)
    return a + b
