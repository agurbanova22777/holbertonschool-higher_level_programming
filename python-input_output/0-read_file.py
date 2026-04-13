#!/usr/bin/python3
"""Read a text file and print to stdout"""


def read_file(filename=""):
    """Reads a text file and print to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
