#!/usr/bin/python3


def search_replace(my_list, search, replace):

    newList = []

    for number in my_list:
        if search == number:
            newList.append(replace)
        else:
            newList.append(number)

    return newList
