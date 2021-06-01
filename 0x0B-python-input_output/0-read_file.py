#!/usr/bin/python3
def read_file(filename=""):
    """ Reads a text file and prints it to stdout """

    with open(filename, encoding='UTF-8') as file:
        print(file.read())
