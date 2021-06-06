#!/usr/bin/python3
'''comments'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''comments'''

    def __init__(self, size):
        '''comments'''
        self.integer_validator("size", size)
        super().__init__(size, size)
