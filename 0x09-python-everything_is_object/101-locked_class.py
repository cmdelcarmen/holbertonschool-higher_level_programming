#!/usr/bin/python3
'''locked class'''


class LockedClass:
    '''define LockedClass with a private
    name attributes'''

    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        '''initializes class'''
        self.first_name = first_name
