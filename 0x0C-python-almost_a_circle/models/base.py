#!/usr/bin/python3
"""
This module is the base class

"""
import json
import csv

class Base:
    """
    This is the Base

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        this function instantiate the base base instance

        Args:
            id (int): the id presented as an argument

        """
        if id is not None:
            if not isinstance(id, int) or id < 1:
                raise ValueError("id must be a positive integer")
            elif Base.__nb_objects >= id:
                raise ValueError("Specified id is already in use")
            elif ob in range(1, Base.__nb_objects + 1):
                if ob == id:
                    raise ValueError("Specified is already in use")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this function returns a JSON string representation
        Args:
            list_dictionaries (list): the list of dictionaries
        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this is a class method that would
        save list of instances to JSON file
        Args:
            list_objs (list): the list of instances

        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                             for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        this function returns the list of the JSON string
        Args:
            json_string (list): the is list argument

        """
        if json_string is None or not json_string:
            "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        this class method create an instance with all
        attributes already set
        Args:
            **dictionary (dict): dictionary with all attributes names
        Returns:
            Base: An instance with all attributes set
            based on the values from the dic

        """
        if cls.__name__ == "Rectangle":
            fake_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            fake_inst = cls(1)
        else:
            raise ValueError("Invalid class name")
        fake_inst.update(**dictionary)
        return fake_inst

    def update(self, *args, **kwargs):
        """
        this method updates the attributes

        """
        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    @classmethod
    def load_from_file(cls):
        """
        this class method returns a list of instances from a JSON file

        Returns:
            list: A list of instances created from JSON file

        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        the class method to serialize instances to a CSV file.
        Args:
            list_objs (list): A list of instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fields = ["id", "size", "x", "y"]
            else:
               fields = []
            writer.writerow(fields)
            for obj in list_objs:
                writer.writerow([getattr(obj, field) for field in fields])
    
    @classmethod
    def load_from_file_csv(cls):
        """
        the method to deserialize instances from a CSV file

        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, newline='') as file:
                reader = csv.reader(file)
                fields = next(reader, [])
                instances = []
                for row in reader:
                    dictionary = {field: int(value) for field, value in zip(fields, row)}
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return []
