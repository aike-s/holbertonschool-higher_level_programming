#!/usr/bin/python3
"""
In this module a function showing the representation
of an object in a dictionary
"""


def class_to_json(obj):
    """  returns the dictionary description of a class """

    return obj.__dict__
