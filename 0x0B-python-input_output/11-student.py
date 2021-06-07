#!/usr/bin/python3
'''comments'''


class Student:
    '''comments'''

    def __init__(self, first_name, last_name, age):
        '''comments'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''comments'''

        attrs_dict = {}

        if type(attrs) is list:
            if all(type(element) is str for element in attrs):
                for key in self.__dict__:
                    if key in attrs:
                        attrs_dict[key] = self.__dict__[key]
                return attrs_dict

        return self.__dict__

    def reload_from_json(self, json):
        '''comments'''
        for key, value in json.items():
            self.__dict__[key] = value
