#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    newMatrix = []
    secondMatrix = []
    thirdMatrix = []

    if len(matrix) == 0:
        return None

    for x in range(1):
        for y in range(len(matrix)):
            squaredMatrixValue = ((matrix[x][y]) ** 2)
            newMatrix.append(squaredMatrixValue)

    for x in range(1, 2):
        for y in range(len(matrix)):
            squaredMatrixValue = ((matrix[x][y]) ** 2)
            secondMatrix.append(squaredMatrixValue)

    for x in range(2, 3):
        for y in range(len(matrix)):
            squaredMatrixValue = ((matrix[x][y]) ** 2)
            thirdMatrix.append(squaredMatrixValue)

    newMatrix = [newMatrix, secondMatrix, thirdMatrix]
    return newMatrix
