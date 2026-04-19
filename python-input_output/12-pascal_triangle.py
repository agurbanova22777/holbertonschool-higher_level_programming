#!/usr/bin/python3
"""Generate Pascal's triangle up to n rows."""


def pascal_triangle(n):
    """Return a list of lists of integers for Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
