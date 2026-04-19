#!/usr/bin/env python3
"""Pickle-based serialization/deserialization for a custom class."""

import pickle


class CustomObject:
    """Custom object that can be serialized/deserialized using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Return None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError, AttributeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return a CustomObject instance from a pickle file.

        Return None if the file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, EOFError, pickle.UnpicklingError, AttributeError):
            return None
