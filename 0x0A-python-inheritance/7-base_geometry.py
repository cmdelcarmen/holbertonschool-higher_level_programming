#!/usr/bin/python3
'''comments'''


class BaseGeometry:
    '''comments'''

    def area(self):
        '''comments'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''comments'''
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
