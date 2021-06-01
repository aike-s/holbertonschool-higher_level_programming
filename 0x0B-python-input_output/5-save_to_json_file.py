#!/usr/bin/python3
"""
In this module a function to convert an object into text
with JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation: """

    with open(filename, mode='a+', encoding='UTF-8') as file:
        text = json.dumps(my_obj)
        file.write(text)
