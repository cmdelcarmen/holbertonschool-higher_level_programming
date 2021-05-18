#!/usr/bin/python3


class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for count in range(0, self.__size):
            for count2 in range(0, self.__size):
                print("#", end="")
            print()

        if self.__size == 0:
            print()
