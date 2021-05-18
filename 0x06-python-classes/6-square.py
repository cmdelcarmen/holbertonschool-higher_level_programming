#!/usr/bin/python3


class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):

        print(self.__position)

        for count in range(0, self.__size):
            for count2 in range(0, self.__size):
                if count2 == 0:
                    for count3 in range(0, self.__position[0]):
                        print(" ", end="")
                print("#", end="")
            print()

        if self.__size == 0:
            print()
