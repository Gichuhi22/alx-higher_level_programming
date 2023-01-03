#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """
    sets the value of width and height
    raises:
        TypeError if either height or width is not an integer
        ValueError if width or height is less than 0
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Heiight must be >= 0")
        self.__height = value
