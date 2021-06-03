#!/usr/bin/python3
"""
In this module a class Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Creating a class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initialization of class Rectangle """

        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__heigth = height

    def area(self):
        """ Returns the area of a Rectangle object """

        return (self.__width * self.__heigth)

    def __str__(self):
        """ Prints a reprsentation of an object of class Rectangle """

        return ("[Rectangle] {}/{}".format(self.__width, self.__heigth))
