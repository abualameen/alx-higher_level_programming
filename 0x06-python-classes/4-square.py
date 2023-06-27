#!/usr/bin/python3
class Square:

    """
        this class defines a Square, with a private instance attribute size
    """
    def __init__(self, size=0):

        """
        This function initializes the attribute size
       
        """
        self.__size = size

    @property
    def size(self):
        """
        this function retrieve the attribute size

        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        this function sets the size attribute to a value 
        that as to be an integer, it raises various error based on the val provided
        
        """
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        """
        This function computes the area of a square

        """
        return (self.__size * self.__size)
