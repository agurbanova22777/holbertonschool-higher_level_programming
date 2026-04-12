#!/usr/bin/python3
"""Define MyList class that inherits from list and can print itself sorted."""


class MyList(list):
    """A list subclass with a method to print elements sorted ascending."""

    def print_sorted(self):
        """Print the list in ascending sorted order (without modifying self)."""
        print(sorted(self))
