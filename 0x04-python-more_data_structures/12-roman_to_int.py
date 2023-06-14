#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str)) or len(roman_string) == 0:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom = dic[roman_string[0]]
    for i in range(1, len(roman_string)):
        if dic[roman_string[i - 1]] >= dic[roman_string[i]]:
            rom += dic[roman_string[i]]
        else:
            rom += dic[roman_string[i]] - (2 * dic[roman_string[i - 1]])
    return rom
