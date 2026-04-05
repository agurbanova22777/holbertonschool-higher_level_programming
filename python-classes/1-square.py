#!/usr/bin/python3
"""Define a Square class with a private size attribute."""


class Square:
    """Square class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: Size of the square (no type/value verification in this task).
        """
        self.__size = size
