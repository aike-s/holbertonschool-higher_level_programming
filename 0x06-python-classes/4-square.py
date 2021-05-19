#!/usr/bin/python3

"""Defining a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):

        """Initializes square"""
        self.__size = size

    @property
    def size(self):

        """Property"""
        return self.__size

    @size.setter
    def size(self, value):

        """Handle except errors"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''Calculate the area of a square'''
        return (self.__size * self.__size)
