#!/usr/bin/python3
'''comments'''


from models.base import Base
import sys


class Rectangle(Base):
    '''comments'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''comments'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
            '''comments'''
            return self.__width

    @width.setter
    def width(self, value):
        '''comments'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''comments'''
        return self.__height

    @height.setter
    def height(self, value):
        '''comments'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''comments'''
        return self.__x

    @x.setter
    def x(self, value):
        '''comments'''
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''comments'''
        return self.__y

    @y.setter
    def y(self, value):
        '''comments'''
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        '''comments'''
        return self.__width * self.__height

    def display(self):
        '''comments'''
        for y in range(0, self.__y):
            print()

        for height in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for width in range(0, self.__width):
                print('#', end="")
            print()

    def __str__(self):
        '''comments'''
        str_rectangle = "[Rectangle] "
        str_rectangle += "({}) ".format(self.id)
        str_rectangle += "{}/{} ".format(self.__x, self.__y)
        str_rectangle += "{}/{}".format(self.__width, self.__height)
        return str_rectangle

    def update(self, *args):
        '''comments'''
        counter = 0

        if len(sys.argv) > 1:
            self.width = int(sys.argv[1])
            self.height = int(sys.argv[2])
            self.x = int(sys.argv[3])
            self.y = int(sys.argv[4])
            self.id = int(sys.argv[5])
        else:
            for argument in args:
                if counter == 1:
                    self.width = argument

                if counter == 2:
                    self.height = argument

                if counter == 3:
                    self.x = argument

                if counter == 4:
                    self.y = argument

                if counter == 0:
                    self.id = argument
                counter += 1
