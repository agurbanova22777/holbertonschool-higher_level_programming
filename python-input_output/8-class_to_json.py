#!/usr/bin/python3
"""Return a JSON-serializable dict description of an object."""


def class_to_json(obj):
    """Return a dict description for JSON serialization."""
    return obj.__dict__
