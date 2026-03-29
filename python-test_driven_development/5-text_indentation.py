#!/usr/bin/python3
"""Print text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    chars = ".?:"
    i = 0
    while i < len(text):
        if text[i] in chars:
            print(text[i], end="")
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        if text[i] == " " and (i == 0 or text[i - 1] in chars):
            i += 1
            continue

        print(text[i], end="")
        i += 1
