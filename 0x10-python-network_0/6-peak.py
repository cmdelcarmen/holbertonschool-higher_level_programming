#!/usr/bin/python3
""" Write a function that finds a peak in a
    list of unsorted integers. """


def find_peak(list_of_integers):
    """ Method finds a peak in a list of
    unsorted integers. """

    array = list_of_integers

    if array:

        if len(array) == 1:
            return array[0]

        if len(array) == 2:
            return max(array)

        middle = int((len(array) - 1) / 2)

        if array[middle] < array[middle + 1]:
            return find_peak(array[middle + 1:])
        else:
            return find_peak(array[:middle + 1])

    else:
        return None
