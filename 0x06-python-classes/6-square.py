#!/usr/bin/python3

"""
    this module defines a square class

"""


class Square:

    """
        this class defines a Square, with a private instance attribute size
    """
    def __init__(self, size=0, position=(0, 0)):

        """
        This function initializes the square instance.
        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square where
            the (defualt is (0, 0))
        """
        self.size = size
        self._position = position

    @property
    def size(self):

        """
        this function retrieve the attribute size.

        Returns:

            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, val):

        """
        this function sets the size
        attribute to a value
        that as to be an integer, it raises various
        error based on the val provided
        Args:
            val (int): The size of the square.
        Raises:
            TypeError: If the val is not an integer.
            ValueError: If the val is less than 0.

        """
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    @property
    def position(self):
        """
        this getter capability retrieves the position of the square
        Returns:
            tuple: The square position

        """
        return self._position

    @position.setter
    def Position(self, val):
        """
        this setter function set the position of the square
        Args:
            val (tuple): The position of the square
        Raises:
            TypeError: if the value is not a tuple or contains non interger ele
            ValueError: if val is more than two ele
         """
        if not isinstance(val, tuple) or len(val) != 2:
            raise TypeError("position must be taplue ot two int")
        elif not all(isinstance(ele, int) for ele in val):
            raise TypeError("elem in position should be an int")
        else:
            self._position = val

    def area(self):
        """
        This function computes the area of a square
        Returns:
            int: The area of the square

        """
        return (self.__size * self.__size)

    def my_print(self):

        """
        Prints the square with the character '#' to the stdout.
        If size is  0. prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for h in range(self._position[1]):
                print()
            for k in range(self.__size):
                print(" " * self._position[0] + "#" * self.__size)
