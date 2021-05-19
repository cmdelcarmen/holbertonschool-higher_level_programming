#!/usr/bin/python3
'''This module defines an object class called Square'''


class Square:
    '''This class contains a size attribute'''
    def __init__(self, size=0):
        ''' This metho init the class'''
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size
        else:
            raise TypeError("Size must be an integer")
