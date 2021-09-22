#!/usr/bin/python3
'''
    Write a function that deletes the item at a specific position in a list.
'''
def delete_at(my_list=[], idx=0):

    new_list = my_list

    if idx < 0:
        return my_list

    if idx > (len(my_list) - 1):
        return my_list

    del new_list[idx]

    return new_list
