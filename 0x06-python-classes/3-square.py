#!/usr/bin/python3

"""Defining a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):

        """Initializes square"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):

        """Calculates the area of the square"""
        return (self.__size * self.__size)
