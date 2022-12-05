#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    newlist = my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
        exit()
    else:
        del newlist[idx]
    return newlist
