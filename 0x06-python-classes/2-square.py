#!/usr/bin/python3

"""Defining a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):

        """Initializes the square"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
