#!/usr/bin/python3
"""
In this module the class Rectangle that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ Tha class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """ Initialization fo the Rectangle attributes """
        Base.__init__(self, id)
        self.__width = width
        self.__height  = height
        self.__x  = x
        self.__y  = y


    @property
    def width(self):

        """ Returns the attribute value """
        return self.__width

    @width.setter
    def width(self, width):

        """ Assigns the parameter to the attribute after filtering """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = self.width

    @property
    def height(self):

        """ Returns the attribute value """
        return self.__height

    @height.setter
    def height(self, height):

        """ Assigns the parameter to the attribute after filtering """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = self.height

    @property
    def x(self):

        """ Returns the attribute value """
        return self.__x

    @x.setter
    def x(self, x):

        """ Assigns the parameter to the attribute after filtering """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = self.x

    @property
    def y(self):

        """ Returns the attribute value """
        return self.__y

    @y.setter
    def y(self, y):

        """ Assigns the parameter to the attribute after filtering """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = self.y

    def area(self):

        """ Method to find the area of a Rectangle instance """
        return (self.__height * self.__width)

    def display(self):

        """ Method that prints in stdout the Rectangle instance """
        # First the height is printed
        for y in range(0, self.__y): print()
        for y in range(0, self.__height):

            # Now the width is printed
            for x in range(0, self.__x): print (' ', end='') 
            for x in range(1, self.__width): print('#', end='')

            # This is part of the height, it has to be printed after the width
            # to start each row
            print('#')

    def __str__(self):

        """ Method for represent an instance in a string  """
        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):

        """ Method for update the class Rectangle """
        attributes_list = ["id", "__width", "__height", "__x", "__y"]

        if args is not None:
            for i, value in enumerate(args):
                setattr(self, attributes_list[i], value)

        elif kwargs is not None:
            for key, value in kwargs.items():
                # The following validation is to check if the object
                # has this attribute or not
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):

        """ Returns the dictionary representation of a Rectangle instance"""
        return {"id" : self.id, "width" : self.__width, "height" : self.__height, 
        "x" : self.__x, "y" : self.__y}
