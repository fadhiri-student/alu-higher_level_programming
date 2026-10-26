#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    previous = 0
    for char in reversed(roman_string):
        if char not in values:
            return 0
        if values[char] < previous:
            total -= values[char]
        else:
            total += values[char]
            previous = values[char]
    return total
