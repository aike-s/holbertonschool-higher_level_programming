#!/usr/bin/python3
"""
In this module a function to represent an object in JSON strings
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string) """

    return json.dumps(my_obj)
