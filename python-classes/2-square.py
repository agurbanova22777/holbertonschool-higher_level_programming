#!/usr/bin/python3
"""Define a Square class with validated private size attribute."""


class Square:
    """Square class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Size of the square (default: 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
