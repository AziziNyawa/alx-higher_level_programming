#!/usr/bin/python3
"""This module defines a class Student """


class Student:
    """Defines a class of Student
    """

    def __init__(self, first_name, last_name, age):
        """Intializing the instances of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict representation of the 
        """
        return self.__dict__
