#!/usr/bin/python3
"""
this module is a class Student that defines a student

"""


class Student:
    """
    this class is a student class

    """
    def __init__(self, first_name, last_name, age):
        """
        this method instantials a student instance
        Args:
            fist_name (str): the students first name
            last_name (str): ths students last name

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        this method that retrieves a dictionary representation
        of a Student instance

        """
        if attrs is not None:
            if not isinstance(attrs, list):
                raise ValueError("attrs must be a list of strings")
            if not all(isinstance(attr, str) for attr in attrs):
                raise ValueError("attrs must be a list of strings")
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}


    def reload_from_json(self, json):
        """
        that replaces all attributes of the Student instance

        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
