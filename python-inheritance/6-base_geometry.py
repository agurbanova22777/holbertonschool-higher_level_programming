#!/usr/bin/python3
"""Define BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raise an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")
