#!/usr/bin/python3
'''File contains matrix_divided function'''


def matrix_divided(matrix, div):

    '''Matrix_divided - funtion divides all elements of a matrix,
        by the second parameter passed to the function. It creates
        a new matrix to hold new values.

        Returns: the new matrix'''


    '''matrix input validation'''
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
            if len(row) is not len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for element in row:
            if not type(element) is int and not type(element) is float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    '''div input validation'''
    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = list(map(list, matrix))

    for idx1 in range(0, len(matrix)):
        for idx2 in range(0, len(matrix[0])):
            newMatrix[idx1][idx2] = float("{:.2f}".format(matrix[idx1][idx2] / div))

    return (newMatrix)
