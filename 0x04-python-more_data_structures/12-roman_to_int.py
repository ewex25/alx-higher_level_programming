#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if (type(roman_string) is not str or roman_string is None):
        return (0)
    for i, char in enumerate(roman_string):
        tmp_val = roman[char]
        try:
            if tmp_val < roman[roman_string[i + 1]]:
                tmp_val = tmp_val * -1
        except IndexError:
            pass
        num = num + tmp_val
    return (num)
