#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j, n in enumerate(row):
            end = " " if j != len(row) - 1 else ""
            print("{:d}".format(n), end=end)
        print()
