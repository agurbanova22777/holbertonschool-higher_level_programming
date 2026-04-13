#!/usr/bin/python3
"""This module appends a string to utf8 and returns num of chars"""


def append_write(filename="", text=""):
    """Write a string to utf8 and return num of chars"""
    with open(filename, 'a', encoding="utf8") as f:
        return f.write(text)
