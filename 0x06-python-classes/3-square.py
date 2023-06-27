#!/usr/bin/python3


"""
    this module defines a square class
"""


class Square:

    """
        this class defines a Square, with a private instance attribute size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
        this

    """
    def area(self):
        return (self.__size * self.__size)
