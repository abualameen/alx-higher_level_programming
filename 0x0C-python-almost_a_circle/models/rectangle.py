#!/usr/bin/python3
"""
this module creates a rectangle class

"""
from models.base import Base


class Rectangle(Base):
    """
    this is a rectangle class that inherites from the base class

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
         This function initializes the rectangle instance.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0)
            x (int): is an attribute of the rectangle class
            y (int): is an attribute of th rectangle class

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        This function retrieves the attribute width
        Returns:
            int: the width of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        this function sets the width attribute to a value
        , val has to be an integer, it raised various
        based on the val provided
        Args:
            val (int): The width of the rectangle
        Raises:
            TypeError: if the val is not an integer
            ValueError: If the val is less than 0

        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """
        This function retrieves the attribute height
        Returns:
            int: The height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        this function sets the height attribute to a value
        , val has to be an integer, it raised various
        based on the val provided
        Args:
            val (int): The height of the rectangle
        Raises:
            TypeError: if the val is not an integer
            ValueError: If the val is less than 0

        """
        if not isinstance(val, int) or not isinstance(val, (int, float)):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """
        This function retrieves the attribute x
        Returns:
            int: value of x

        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        this function sets the x attribute to a value
        , val has to be an integer, it raised various
        based on the val provided
        Args:
            val (int): The x value
        Raises:
            TypeError: if the val is not an integer
            ValueError: If the val is less than 0

        """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """
        This function retrieves the attribute y
        Returns:
            int: the value of y

        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        this function sets the y attribute to a value
        , val has to be an integer, it raised various
        based on the val provided
        Args:
            val (int): The y value of the rectangle
        Raises:
            TypeError: if the val is not an integer
            ValueError: If the val is less than 0

        """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """
        compute the area of the rectangle

        """
        return self.__width * self.__height

    def display(self):
        """
        displays the instance of the rectangle with #

        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            x_cod = ' ' * self.x
            hassh = '#' * self.width
            line = x_cod + hassh
            print(line)

    def __str__(self):
        """
        return string reps of the rectangle

        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        this function assigns an argument to each attribute
        Args:
            no.1 argument = id attribute
            no.2 argument = width attribute
            no.3 argument = height attribute
            no.4 argument = x attribute
            no.5 argument = y attribute

        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        This function returns a dictionary representation
        of the rectangle
        Returns:
            dict: A dictionary represatio of a rectangle
                with it attributes

        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
