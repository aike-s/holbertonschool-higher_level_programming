#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
        with open(filename, mode='a+', encoding='UTF-8') as file:
                text = json.dumps(my_obj)
                file.write(text)
