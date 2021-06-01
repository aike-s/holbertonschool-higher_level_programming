#!/usr/bin/python3
"""
In this module the class Student
"""


class Student:
    """ Defining a student """

    def __init__(self, first_name, last_name, age):
        """ Initialization of a student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student """

        return self.__dict__
