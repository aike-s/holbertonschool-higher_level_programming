#!/usr/bin/python3
""" Module """


def magic_string():
    """ Magic string """
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return ", ".join(["Holberton" for i in range(magic_string.counter)])
