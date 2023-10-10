#!/usr/bin/python3
"""Defining the '12-pascal_triangle' module"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    tri = [[1]]

    for i in range(n):
        t = tri[-1]
        m = [1]

        for j in range(len(t) - 1):
            m.append(t[j] + t[j + 1])

        m.append(1)
        tri.append(m)

    return tri
