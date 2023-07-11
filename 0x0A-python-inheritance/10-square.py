#!/usr/bin/python3
"""
This module creates an empty class

"""


class BaseGeometry:
    """
    This is a base class

    """
    def area(self):
        """
        this function computes the area of a shape

        Raises:
            Exception: Show that the method is not implemented
            in the subclass

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates the value of as an integer

        Args:
            name (str): The name of the value to be validated
            value: The value being validated

        Raises:
            TypeError: with the message "name must be an integer
            ValueError: with the message "name must be greater than 0"

        """
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if not value:
            raise TypeError(f"{name} must be an integer")


class Rectangle(BaseGeometry):
    """
    this class is a rectangle object class

    """
    def __init__(self, width, height):
        """
        this method instantials the width and height of the rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the ractangle

        Raises:
            ValueError: when the width and height is not a positive integer

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        this method compute the area of the rectangle and returns it

        Returns:
            int: The area of the rectangle

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle

        Returns:
            str: The string representation of the ractangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    this class is a square object class

    Attributes:
    - _size (int): The size of the square

    """
    def __init__(self, size):
        """
        this method instantiates the intance of the square class
        Args:
            size: this size of the square
        Raises:
            ValueError: if size is not a positive integer

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
