#!/usr/bin/python3
"""
In this module a single function to make a list of all the atributtes
and methods of an object
"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object """

    return dir(obj)
