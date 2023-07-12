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

    def to_json(self):
        """
        this method that retrieves a dictionary representation
        of a Student instance

        """
        if hasattr(self, '__dict__'):
            return self.__dict__
        else:
            return {}
