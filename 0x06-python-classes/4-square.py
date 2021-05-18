#!/usr/bin/python3
'''This module defines an object class called Squares'''


class Square:
    '''This class contains a private attribute called class'''
    def __init__(self, size=0):
        '''Initializes private class attribute size'''
        self.__size = size

    def area(self):
        '''Class method returns area'''
        return (self.__size * self.__size)

    @property
    def size(self):
        '''Class method returns value of instance'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Class method returns value of instance'''
        try:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be integer")
