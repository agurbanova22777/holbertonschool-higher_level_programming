#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in roman_string[::-1]:
        val = r.get(ch, 0)
        total += -val if val < prev else val
        prev = val
    return total
