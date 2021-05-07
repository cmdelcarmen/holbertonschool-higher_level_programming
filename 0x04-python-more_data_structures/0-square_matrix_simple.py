#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    newMatrix = []

    for row in range(len(matrix)):
        newMatrix.append(list(map(lambda x: x ** 2, matrix[row])))

    return(newMatrix)
