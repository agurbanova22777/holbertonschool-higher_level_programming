#!/usr/bin/python3
"""Function to return the list of available attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of obj."""
    return dir(obj)
