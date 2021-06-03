#!/usr/bin/python3
"""
In this module a a class MyList that inherits from list
"""


class MyList(list):
    """ Handle lists """

    def print_sorted(self):
        """ Prints the list, but sorted """

        print(sorted(self))
