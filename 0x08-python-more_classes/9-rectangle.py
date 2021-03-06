#!/usr/bin/python3
'''File contains Rectangle class'''


class Rectangle:
    '''defines a class named Rectangle
    that takes a width and a height'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''creates an instance of a class'''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''returns width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''validates width input and defines it'''
        if not type(value) is int:
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''returns height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''validates height input and defines it'''
        if not type(value) is int:
            raise TypeError("heigth must be integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

    def area(self):
        '''returns area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns perimeter of rectangle'''
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''returns string made up of '#' in the shape/size
        of the rectangle'''

        str_rectangle = ""

        for y in range(0, self.height):
            for x in range(0, self.width):
                str_rectangle += self.print_symbol.__str__()
            if (y + 1) < self.height:
                str_rectangle += '\n'

        return (str_rectangle)

    def __repr__(self):
        '''returns width and heigth of rectangle'''
        return ("Rectangle({}, {})".format(self.__height, self.__width))

    def __del__(self):
        '''prints message when object is deleted'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns biggest rectangle based on area'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance where width/heigth == size'''
        if not type(size) is int:
            raise TypeError("width must be integer")
        if size < 0:
            raise ValueError("width must be >= 0")

        return (cls(size, size))
