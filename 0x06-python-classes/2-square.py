#!/usr/bin/python3
'''This module defines an object class called Square'''


class Square:
    '''This class contains a size attribute'''
    def __init__(self, size=0):
        ''' This metho init the class'''
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
