#!/usr/bin/python3
"""
In this module a class BaseGeometry
"""


class BaseGeometry:
    """ Creating a class BaseGeometry """

    def area(self):
        """ Method with raise exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if the value attribute is an integer or not """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
