#!/usr/bin/python3
'''This module defines an object class called Squares'''


class Square:
    '''This class contains a private attribute called class'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initializes private class attributes size and position'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Method returns value of instance '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Method returns value of instance '''
        if not type(value) is int:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Method returns value of instance '''
        return self.__position

    @position.setter
    def position(self, value):
        '''Method returns '''
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position

    def area(self):
        ''' This method returns the area'''
        return (self.__size * self.__size)

    def my_print(self):
        '''This method pritns the square '''

        for count in range(0, self.position[1]):
            print()

        for count in range(0, self.__size):
            for count2 in range(0, self.__size):
                if count2 == 0:
                    for count3 in range(0, self.__position[0]):
                        print(" ", end="")
                print("#", end="")
            print()

        if self.__size == 0:
            print()
