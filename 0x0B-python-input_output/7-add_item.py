#!/usr/bin/python3
"""
In this file a main for add arguments to a Python list and save them in a file
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    try:
        object_from_json = load_from_json_file("add_item.json")
    except:
        pass
        object_from_json = []
    for to_add in argv[1:]:
        object_from_json.append(to_add)
    save_to_json_file(object_from_json, "add_item.json")
