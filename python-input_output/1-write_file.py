#!/usr/bin/python3
"""This module Writes a string to utf8 and return num of chars"""


def write_file(filename="", text=""):
    """Write a string to utf8 and return num of chars"""
    with open(filename, 'w', encoding="utf8") as f:
        return f.write(text)
