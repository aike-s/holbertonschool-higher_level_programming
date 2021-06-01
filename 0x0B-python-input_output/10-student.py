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

        # Here the dictionary is initializated
        for_dict = {}
        if type(attrs) == list:
            # Now the list is scrolling
            for index_attribute in attrs:
                # And it is looked for if the attribute that is in that
                # position is also in the general dictionary of the class
                if index_attribute in self.__dict__:
                    # If so, it is added to the previously
                    # initialized dictionary
                    for_dict[index_attribute] = self.__dict__[index_attribute]

        # The created dictionary is returned
        return for_dict
