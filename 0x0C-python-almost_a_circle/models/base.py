#!/usr/bin/python3
"""
In this module the class Base
"""
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):

        """ Initialization of the Base attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):

        """ Writes the JSON string representation of list_objs into a file """
        # To start, look for the class name of the instance in the list
        # to name the file to be written to
        # Example: Class_name.json
        class_name = cls.__name__, list_objs[0]
        filename = class_name[0] + ".json"

        # Make a list with dictionary for each object passed to us in list_obj
        list_dict = []
        for obj in list_objs:
            list_dict.append(vars(obj))

        # Then, make a JSON string representation of the list
        # with the to_json_string method and save it in 'text'
        text = cls.to_json_string(list_dict)
        with open(filename, mode='w', encoding='UTF-8') as open_file:
            # Now 'text' will be written to the file.
            open_file.write(text)

    @staticmethod
    def from_json_string(json_string):

        """ Returns the list of the JSON string representation """
        json_list = []

        if json_string is not None or len(json_string) != 0:
            json_list.append(json_list)

        return json_list
