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

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student """

        if attrs is None:
            return self.__dict__

        for_dict = {}
        if type(attrs) == list:
            for index_attribute in attrs:
                if index_attribute in self.__dict__:
                    for_dict[index_attribute] = self.__dict__[index_attribute]

        return for_dict

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """

        self.__dict__.update(json)
