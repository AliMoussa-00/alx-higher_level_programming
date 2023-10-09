#!/usr/bin/python3
"""Defining the '1-my_list' module"""

class MyList(list):
    """Defining the MyList class"""

    def print_sorted(self):
        """ Implementing the 'print_sorted' fucntion to sort a list"""

        print(sorted(self))
