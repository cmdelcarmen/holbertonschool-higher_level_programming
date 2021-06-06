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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
