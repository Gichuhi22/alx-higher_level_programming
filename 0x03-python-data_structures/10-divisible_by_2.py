#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    newlist = my_list[:]
    i = 0
    while i < len(newlist):
        if newlist[i] % 2 == 0:
            newlist[i] = True
        else:
            newlist[i] = False
        i += 1
    return newlist
