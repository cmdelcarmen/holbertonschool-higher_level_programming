#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    newList = []
    newMatrix = []

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            newList.append(matrix[x][y] ** 2)
        newMatrix += [newList]
        newList = []

    return(newMatrix)
