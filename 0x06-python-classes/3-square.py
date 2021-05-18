#!/usr/bin/python3
'''This module defines an object class called Squares'''


class Square:
    '''This class contains a private attribute called class'''
    def __init__(self, size=0):
        '''Initializes private class attribute size'''

        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Calculates area is Square instance'''
        return (self.__size * self.__size)
