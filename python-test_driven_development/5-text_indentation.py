#!/usr/bin/python3
"""Print text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    There will be no spaces at the beginning or end of each printed line.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    seps = ".?:"
    start = 0
    parts = []

    for i, ch in enumerate(text):
        if ch in seps:
            segment = text[start:i + 1].strip()
            parts.append(segment)
            start = i + 1

    tail = text[start:].strip()
    if tail:
        parts.append(tail)

    for idx, part in enumerate(parts):
        print(part, end="")
        if idx != len(parts) - 1:
            print("\n")
