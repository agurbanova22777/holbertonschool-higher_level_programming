#!/usr/bin/python3
"""This module provides a function that adds two numbers as integers."""


def add_integer(a, b=98):
    """Return the sum of a and b after converting floats to integers."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
