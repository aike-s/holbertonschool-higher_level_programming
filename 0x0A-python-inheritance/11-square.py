#!/usr/bin/python3
"""
In this class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Creating class Square """

    def __init__(self, size):
        """ Initialization of class square """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Prints a reprsentation of an object of class Square """

        return ("[Square] {}/{}".format(self.__size, self.__size))
