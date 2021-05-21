#!/usr/bin/python3

"""Defining a rectangle"""


class Rectangle:

    """Represents a class rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        """Initializes rectangle"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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

    def __str__(self):

        """Function for print a matrix in hash"""
        if self.__width == 0 or self.__height == 0:
            return ''
        matrix = ''
        for x in range(self.__height):
            for y in range(self.__width):
                matrix = matrix[:] + str((self).print_symbol)
            if x < self.__height - 1:
                matrix = matrix[:] + '\n'
        return matrix

    def __repr__(self):

        """Makes a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):

        """Msg after delete an object"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """Verify the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError('{} must be an instance of Rectangle'\
                .format(rect_1))
        if type(rect_2) != Rectangle:
            raise TypeError('{} must be an instance of Rectangle'\
                .format(rect_2))
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
