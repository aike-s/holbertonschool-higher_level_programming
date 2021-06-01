#!/usr/bin/python3
"""
In this module a single function to read a file
"""


def read_file(filename=""):
    """ Reads a text file and prints it to stdout """

    with open(filename, mode='r', encoding='UTF-8') as file:
        print(file.read())
