#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        count = 0
        total = 0
        for items in my_list:
            product = 1
            for i in items:
                product *= i
            total += product
            count += items[1]
        return total / count
    else:
        return 0
