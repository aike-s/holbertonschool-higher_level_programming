#!/usr/bin/python3
"""
In this module the Square class that inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square class"""

    def __init__(self, size, x=0, y=0, id=None):

        """ Initialization of the Square attributes """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):

        """ Returns the attribute value """
        return self.width

    @size.setter
    def size(self, width):

        """ Assigns the parameter to the attribute """
        self.width = self.size
        self.height = self.size

    def update(self, *args, **kwargs):

        """ Method for update the class Rectangle """
        attributes_list = ["id", "size", "x", "y"]

        if args is not None:
            for i, value in enumerate(args):
                setattr(self, attributes_list[i], value)
        elif kwargs is not None:
            for key, value in kwargs.items():
                # The following validation is to check if the object
                # has this attribute or not
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):

        """ Method for represent an instance in a string  """
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width))

    def to_dictionary(self):

        """ Returns the dictionary representation of a Square instance"""
        return {"id" : self.id, "size" : self.width,
        "x" : self.x, "y" : self.y}
