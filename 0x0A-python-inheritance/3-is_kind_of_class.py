#!/usr/bin/python3
"""
In this module a single function if an object is an instance of,
or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """Returns true or false if the condition is met or not met respectively"""

    return isinstance(obj, a_class)
