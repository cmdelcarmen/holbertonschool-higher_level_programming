#!/usr/bin/python3
'''This module defines an object class called Squares'''


class Square:
    '''This class contains a private attribute called class'''
    def __init__(self, size=0):
        '''Initializes private class attribute size'''
        self.__size = size

    @property
    def size(self):
        '''Class method returns value of instance '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Class method returns value of instance'''
        if not type(value) is int:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Method returns the area of the Square instance'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Method prints out set'''
        for count in range(0, self.__size):
            for count2 in range(0, self.__size):
                print("#", end="")
            print()

        if self.__size == 0:
            print()
