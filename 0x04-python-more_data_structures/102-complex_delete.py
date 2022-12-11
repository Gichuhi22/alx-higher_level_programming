#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newlist = []
    if value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if val == value:
                newlist.append(key)

        for items in newlist:
            if items in a_dictionary:
                del a_dictionary[items]
        return a_dictionary
