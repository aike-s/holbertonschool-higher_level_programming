#!/usr/bin/python3

"""Defining a rectangle"""


class Rectangle:

    """Represents a class rectangle"""

    def __init__(self, width=0, height=0):

        """Initializes rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):

        """Initializates property width"""
        return self.__width

    @width.setter
    def width(self, value):

        """Handle except errors"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):

        """Initializates property height"""
        return self.__height

    @height.setter
    def height(self, value):

        """Handle except errors"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):

        """Calculates the area of a rectangle"""
        total_area = (self.__width * self.__height)
        return total_area

    def perimeter(self):

        """Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            total_perimeter = 0
        else:
            total_perimeter = (self.__width + self.__height) * 2
        return total_perimeter
