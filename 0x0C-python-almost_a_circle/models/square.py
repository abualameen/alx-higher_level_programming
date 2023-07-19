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

    @property
    def size(self):
        """
        retrieves the size attribute

        Returns:
            int: size of the square

        """
        return self.width

    @size.setter
    def size(self, val):
        """
        sets the size of the attribute
        Args:
            value (int): new size value to set.

        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        updates the class square

        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self):
        """
        returns formated string for the square
        Returns:
            str: A formated string representation of the square object

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        this function returns a dic rep of a square instance

        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }
