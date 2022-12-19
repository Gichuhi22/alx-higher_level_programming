#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        roman_string = roman_string.lower()
        r = {"i": 1, "v": 5, "x": 10, "l": 50,
             "c": 100, "d": 500, "m": 1000}
        i = len(roman_string) - 1
        output = 0
        while i >= 0:
            if i < len(roman_string) - 1 and r[roman_string[i]] < r[roman_string[i + 1]]:
                output -= r[roman_string[i]
            else:
            output += r[roman_string[i]]
            i -= 1
            return (output)
    else:
        return (0)
