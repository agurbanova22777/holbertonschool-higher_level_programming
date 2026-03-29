#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div and rounded to 2 decimals.

    Args:
        matrix (list of lists): a matrix of integers/floats (rows must be same size)
        div (int or float): the divisor (must not be zero)

    Raises:
        TypeError: if matrix is not a matrix (list of lists) of integers/floats
        TypeError: if each row of the matrix does not have the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0

    Returns:
        list of lists: new matrix with divided values rounded to 2 decimals
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = None
    new_matrix = []

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
