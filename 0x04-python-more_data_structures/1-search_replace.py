#!/usr/bin/python3
'''
    Write a function that replaces all occurrences of an element by another in a new list.
'''
def search_replace(my_list, search, replace):

    newList = []

    for number in my_list:
        if search == number:
            newList.append(replace)
        else:
            newList.append(number)

    return newList
