#!/usr/bin/python3
'''This module creates a singly linked list'''


class Node:
    '''This class creates a Node'''

    def __init__(self, data, next_node=None):
        '''Creates instance of a Node'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''returns value od instance'''
        return self.__data

    @data.setter
    def data(self, value):
        '''inits nstance'''
        pass

    @property
    def next_node(self):
        '''returns next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''inits node'''
        pass


class SinglyLinkedList:
    '''creates singly linked list'''
    def __init__(self):
        '''init linked list'''
        pass

    def sorted_insert(self, value):
        pass
