#!/usr/bin/python3
"""Module that defines add_integer."""


def add_integer(a, b=98):
    """Return the addition of a and b.

    Args:
        a (int or float): First number.
        b (int or float): Second number (default: 98).

    Raises:
        TypeError: If a is not an int or float.
        TypeError: If b is not an int or float.

    Returns:
        int: The sum of a and b after casting floats to ints.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
