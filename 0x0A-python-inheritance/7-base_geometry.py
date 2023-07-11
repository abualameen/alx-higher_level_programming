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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
