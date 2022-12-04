#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ""
        my_string = my_string.lower()

        for item in my_string:
            if item == 'c':
                continue
            else:
                new_string += item
        return new_string
