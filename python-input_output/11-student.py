#!/usr/bin/python3
"""Defines a Student class with JSON serialization and deserialization helpers."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of this Student.

        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace attributes of the Student instance from a dictionary.

        `json` is a dict where keys are attribute names and values are the
        corresponding values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
