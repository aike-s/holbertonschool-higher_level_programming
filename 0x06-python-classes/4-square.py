#!/usr/bin/python3
class Square:
    '''Defining a square'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''Property'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Handle except errors'''
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''Calculate the area of a square'''
        return (self.__size * self.__size)
