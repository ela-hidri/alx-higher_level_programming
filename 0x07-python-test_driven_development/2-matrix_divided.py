#!/usr/bin/python3
"""
Defines a function that divides a matrix

Attributes:
    matrix_divided: divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides a matrix

    Args:
    matrix: matrix to be divided
    div: value to divid with

    Raises:
    TypeError: if matrix value are not int or float
    TypeError: if matrix rows are not of the same size
    TypeError: div is not an int or float
    ZeroDivisionError: div = 0

    returns: martix divided by div
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if (not matrix) and (not isinstance(matrix, list)):
        raise TypeError(message)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(message)
        for j in i:
            if (not isinstance(j, int)) and (not isinstance(j, float)):
                raise TypeError(message)
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new = [[round(i / div, 2) for i in j] for j in matrix]
    return (new)
