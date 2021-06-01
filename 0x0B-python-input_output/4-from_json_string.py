#!/usr/bin/python3
"""
In this module a function to represent a string in an object with JSON
"""
import json


def from_json_string(my_str):
    """ returns an object represented by a JSON string """

    return json.loads(my_str)
