#!/usr/bin/python3
"""Define MyList class."""


class MyList(list):
    """List subclass with a method to print a sorted copy."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
