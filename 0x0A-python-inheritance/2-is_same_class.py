#!/usr/bin/python3
"""Defining the '2-is_same_class' module"""

def is_same_class(obj, a_class):
    """ Implementing a fuction that:
         returns True if the object is exactly an instance of
         the specified class; otherwise False.
    """

    return type(obj) is a_class
