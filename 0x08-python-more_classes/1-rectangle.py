#!/usr/bin/python3
'''File contains Rectangle class'''


class Rectangle:
    '''defines a class named Rectangle
    that takes a width and a height'''

    def __init__(self, width=0, height=0):
        '''creates an instance of a class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''returns width'''
        return self.___width

    @width.setter
    def width(self, value):
        '''validates width input and defines it'''
        if not type(value) is int:
            raise TypeError("width must be integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''returns height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''validates height input and defines it'''
        if not type(value) is int:
            raise TypeError("heigth must be integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value
