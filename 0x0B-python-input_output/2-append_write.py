#!/usr/bin/python3
"""
In this module a single function to write at the end of a file
"""


def append_write(filename="", text=""):
    """ appends a string and returns the number of characters added """

    with open(filename, mode='a+', encoding='UTF-8') as file:
        return file.write(text)
