#!/usr/bin/python3

"""Defining a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):

        """Initializes a square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):

        """Property"""
        return self.__size

    @size.setter
    def size(self, value):

        """Handle except errors for size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):

        """Property"""
        return self.__position

    @position.setter
    def size(self, value):

        """Handle except errors for position"""
        if !(value[1]) or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):

        """Calculate the area of a square"""
        self.__size = (self.__size * self.__size)
        return self.__size

    def my_print(self):

        """Prints a Square in hash"""
        if self.__size == 0:
            print('')
        else:
            for y in range(0, self.__size):
                for x in range(0, self.__size):
                    print('#', end='')
                print('#')
