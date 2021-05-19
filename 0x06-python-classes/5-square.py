#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        self.__size = (self.__size * self.__size)
        return self.__size

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for y in range(0, self.__size):
                for x in range(0, self.__size):
                    print('#', end='')
                print('#')
