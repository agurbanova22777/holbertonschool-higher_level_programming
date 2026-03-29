#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    The function returns a new matrix where each element is divided by ``div``
    and rounded to 2 decimal places.

    Args:
        matrix (list of lists): A matrix of integers/floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of
            integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: A new matrix with divided values rounded to 2 decimals.
    """
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or matrix == []:
        raise TypeError(matrix_err)

    row_size = None
    new_matrix = []

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(matrix_err)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(matrix_err)
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
