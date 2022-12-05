#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        i = my_list[0]

        for item in my_list:
            if item > i:
                i = item
        return i
    else:
        return None
