#!/usr/bin/python3

"""
    this module defines a rectangle class

"""


class Rectangle:

    """
        this class defines a rectangle, with a private
        instance attribute wid ahd height
    """
    def __init__(self, width=0, height=0):

        """
        This function initializes the rectangle instance.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):

        """
        this function retrieve the attribute width.

        Returns:

            int: width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, val):

        """
        this function sets the width
        attribute to a value
        that as to be an integer, it raises various
        error based on the val provided
        Args:
            val (int): width of the rectangle
        Raises:
            TypeError: If the val(width) is not an integer.
            ValueError: If the val(width) is less than 0.

        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = val

    @property
    def height(self):
        """
        Retreives the height of the rectangle.

        Returns:
            int: height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        sets the height of the rectangle.

        Args:
            val (int): the value of the height to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.

        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """
        the method computes the area of a rectangle

        Returns:
            int: the area of the rectangle

        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        this method computes the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width) + 2 * (self.__height))
