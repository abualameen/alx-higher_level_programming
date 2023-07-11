#!/usr/bin/pyhton
"""
this is a Myint module

"""

class MyInt(int):
    """
    MyInt is a subclass of int with inverted ==  and != operators
    """
    def __eq__(self, other):
        """
        Overrides the == operator to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
