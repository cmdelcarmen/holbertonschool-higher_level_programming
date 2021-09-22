#!/usr/bin/python3
'''
Write a function that returns a set of common elements in two sets.
'''
def common_elements(set_1, set_2):

    list1 = set(set_1)
    list2 = set(set_2)
    newSet = {""}
    index = 0

    for word in list1:
        if word in list2:
            newSet.add(word)

    newSet.remove("")
    return newSet
