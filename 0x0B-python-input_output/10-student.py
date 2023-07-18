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

    def to_json(self, attrs=None):
        """returns a dict representation of the student
        if the attrs is a list of str , rep only those attributes 
        included in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
