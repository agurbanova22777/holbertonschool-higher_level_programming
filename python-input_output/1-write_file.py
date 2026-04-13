#!usr/bin/python3
"""Write a string to utf8 and return num of chars"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf8") as f:
        return f.write(text)
