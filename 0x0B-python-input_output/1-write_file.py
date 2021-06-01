#!/usr/bin/python3
def write_file(filename="", text=""):
    """ writes a string to a text file and """
    """ returns the number of characters written """

    with open(filename, mode='w+', encoding='UTF-8') as file:
        return file.write(text)
