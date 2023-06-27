#!/usr/bin/python3
class Square:

    """
        this class defines a Square, with a private instance attribute size
    """
    def __init__(self, size=0):
        self.__size = size
    """
        this

    """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        return (self.__size * self.__size)
