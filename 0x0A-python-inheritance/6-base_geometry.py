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
    pass
