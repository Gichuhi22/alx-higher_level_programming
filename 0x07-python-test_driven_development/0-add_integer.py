#!/usr/bin/python3
"""
defines a add_integer module
nonintegers and nonfloats raise TypeError
Floats are tycasted to ints
"""


def add_integer(a, b=98):
    """Returns the integer sum of two arguments
    Raises: TypeError - if no argument is given, non float or non int argument
    """
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)

    return int(a) + int(b)
