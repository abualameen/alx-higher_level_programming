#!/usr/bin/python3
"""
this is a square module

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    the is the square class, it inherites from the rectangle class

    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns formated string for the square
        Returns:
            str: A formated string representation of the square object

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
