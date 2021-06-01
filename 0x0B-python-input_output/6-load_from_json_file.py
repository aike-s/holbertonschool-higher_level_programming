#!/usr/bin/python3
"""
In this module a function to create an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """

    with open(filename, mode='r') as file:
        text = file.read()
        return json.loads(text)
