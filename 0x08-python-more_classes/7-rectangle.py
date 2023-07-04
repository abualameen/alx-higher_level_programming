#!/usr/bin/python3
"""
    this module defines a rectangle class

"""


class Rectangle:

    """
    this class defines a rectangle, with a private
    instance attribute width ahd height
    and public instance class number_of_instances

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number
        of instances of the class Rectangle

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """
        This function initializes the rectangle instance.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):

        """
        the function returns a human readable format

        Returns:
            A string representation of a rectangle using th # character
            If the width or the height is equal 0,
            function returns an empty string.

        """
        drw_rec = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height - 1):
            drw_rec += str(self.print_symbol) * self.__width + "\n"
        drw_rec += str(self.print_symbol) * self.__width
        return(drw_rec)

    def __repr__(self):
        """
        this function return a string representation of
        the rectangle to be able to recreate a
        new instance by using eval()

        Returns:
            A string that represents a rectangle in a formated way

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        the function prints a bye message when
        an instance of Rectangle is deleted

        """
        print("Bye rectangle ...")
        Rectangle.number_of_instances -= 1
