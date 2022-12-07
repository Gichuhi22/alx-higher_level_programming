#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []

    new_list.append(set(my_list))
    sum = 0
    for item in new_list:
        for i in item:
            sum += i
    return sum
