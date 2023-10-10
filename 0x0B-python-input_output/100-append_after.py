#!/usr/bin/python3
"""Defining the '100-append_after' module"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    """

    lines = ""

    with open(filename, "r") as file:

        for line in file:
            lines += line

            if search_string in line:
                lines += new_string

    with open(filename, "w") as file:
        file.write(text)
