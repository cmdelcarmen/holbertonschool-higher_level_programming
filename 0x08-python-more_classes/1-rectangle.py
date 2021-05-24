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
        """ getter method """
        return self.___width

    @width.setter
    def width(self, value):
        """ setter method """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
