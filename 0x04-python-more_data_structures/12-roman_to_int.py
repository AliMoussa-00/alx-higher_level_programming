#!/usr/bin/python3

from functools import reduce


def roman_to_int(roman_string):

    if roman_string == 'None' or not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    string_dict = {}
    roman_int = 0

    for roman in roman_string:

        if roman not in roman_dict.keys():
            return 0

        if roman in string_dict:
            string_dict.update({roman: string_dict[roman] + roman_dict[roman]})
        else:
            string_dict.update({roman: roman_dict[roman]})

    if max(string_dict, key=string_dict.get) == roman_string[0]:
        roman_int = sum(string_dict.values())

    elif max(string_dict, key=string_dict.get) == roman_string[-1]:
        roman_int = reduce(lambda x, y: x - y, reversed(string_dict.values()))

    else:
        roman_int = 0

    return roman_int
