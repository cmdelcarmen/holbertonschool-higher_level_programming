#!/usr/bin/python3
'''comments'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''comments'''

    def __init__(self, width, height):
        '''comments'''
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.__width = width
        self.__height = height

    def area(self):
        '''comments'''
        return self.__width * self.__height

    def __str__(self):
        '''comments'''

        width = self.__width
        height = self.__height

        return ("[{}] {}/{}".format(self.__class__.__name__, width, height))
