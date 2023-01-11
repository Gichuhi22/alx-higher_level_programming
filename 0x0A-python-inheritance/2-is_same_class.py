#!/usr/bin/python3
"""a is_same_class function module"""


def is_same_class(obj, a_class):
    """Returns true or false if an object belongs to a class
        or not
    """
    return obj.__class__ is a_class
