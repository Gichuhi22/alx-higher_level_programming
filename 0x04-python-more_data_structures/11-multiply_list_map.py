#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    newlist = []
    newlist = list(map(lambda x: number * x, my_list))

    return newlist
