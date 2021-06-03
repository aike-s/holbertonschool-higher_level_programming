#!/usr/bin/python3
"""
In this module a function to check if an object is an instance
of an especific class
"""


def is_same_class(obj, a_class):
    """Returns True or False if the condition is met or not met respectively"""

    return (type(obj) == a_class)
