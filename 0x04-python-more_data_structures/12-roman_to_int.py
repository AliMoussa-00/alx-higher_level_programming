#!/usr/bin/python3

def roman_to_int(roman_string):

    if roman_string == 'None' or not isinstance(roman_string, str):
        return 0
    if len(roman_string) == 0:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    string_dict = {}
    roman_int = 0

    for i in range(len(roman_string)):

        if roman_string[i] not in roman_dict.keys():
            return 0

        if (i != (len(roman_string) - 1) and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):

            roman_int += roman_dict[roman_string[i]] * -1
        else:
            roman_int += roman_dict[roman_string[i]]

    return roman_int
