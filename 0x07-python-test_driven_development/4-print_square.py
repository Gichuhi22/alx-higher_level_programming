#!/usr/bin/python3
""" Defines a function that prints # character square"""


def print_square(size):
    """
        print a square

        Args:
            size: the length size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is None:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
