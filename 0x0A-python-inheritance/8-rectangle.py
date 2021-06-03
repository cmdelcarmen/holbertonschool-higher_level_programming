#!/usr/bin/python3
'''comments'''


class BaseGeometry:
    '''comments'''

    def __init__(self, width, height):
        '''comments'''
        self.__width = width
        self.__height = height

    def area(self):
        '''comments'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''comments'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''comments'''

    def __init__(self, width, height):
        '''comments'''
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.__width = width
        self.__height = height
