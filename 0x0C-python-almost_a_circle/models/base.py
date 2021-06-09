#!/usr/bin/python3
"""
In this module the class Base
"""
import json
import os.path


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs into a file """
        # To start, look for the class name of the instance in the list
        # to name the file to be written to
        # Example: Class_name.json
        filename = cls.__name__ + ".json"

        # Make a list with dictionary for each object passed to us in list_obj
        list_dict = []

        # Check if the list_objs is None or not
        if list_objs:
            for obj in list_objs:
                list_dict.append(cls.to_dictionary(obj))

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

        if json_string and len(json_string) > 0:
            json_list = list(json.loads(json_string))

        return json_list

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        # At first, create an instance
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        if cls.__name__ == "Square":
            obj = cls(1)
        # Now the instance is updated with the arguments in dictionary
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        # To start, look for the class name to name the file to be written to
        # Example: Class_name.json
        filename = (cls.__name__) + ".json"
        list_instances = []

        # If the file exists do...
        if os.path.isfile(filename):
            with open(filename, mode='r', encoding='utf-8') as open_file:
                text = open_file.read()
            list_dict = Base.from_json_string(text)
            # Every element in the list has a dictionary
            for dictionary in list_dict:
                # With each dictionary I must create an instance
                list_instances += [cls.create(**dictionary)]

        return list_instances
