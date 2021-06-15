#!/usr/bin/python3
'''comments'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''comments'''

    def __init__(self, size, x=0, y=0, id=None):
        '''comments'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''comments'''
        str_square = "[Square] "
        str_square += "({}) ".format(self.id)
        str_square += "{}/{} - ".format(self.x, self.y)
        str_square += "{}/{}".format(self.width, self.height)
        return str_square
