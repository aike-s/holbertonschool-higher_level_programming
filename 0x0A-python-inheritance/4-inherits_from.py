#!/usr/bin/python3
"""
In this module a single function to check if the obj
class is a subclass of a_class
"""


def inherits_from(obj, a_class):
    """Returns True or False if the condition is met or not met respectively"""

    if type(obj) != a_class:
        return (issubclass(type(obj), a_class))
    else:
        return False
