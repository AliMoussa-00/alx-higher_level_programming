#!/usr/bin/python3
"""defining the '6-peak' module"""


def find_peak(list_of_integers):
    """defining the peak func"""

    if list_of_integers is not None and len(list_of_integers) > 0:

        list_of_integers.sort(reverse=True)

        return list_of_integers[0]
