#!/usr/bin/python3
def append_write(filename="", text=""):
    """ appends a string and returns the number of characters added """

    with open(filename, mode='a+', encoding='UTF-8') as file:
        return file.write(text)
