#!/usr/bin/python3
""" My_list module
    defines a class that inherits from a list
"""


class MyList(list):
    """defines a class MyList that inherits from list.
    """
    def print_sorted(self):
        """prints elements in a list in ascending order"""

        print(sorted(self))
