#!/usr/bin/python3

for number in range(0, 10):
    for num in range(0,10):
        if num == 9 and number == 9:
            print("{}{}".format(number, num))
        else:
            print("{}{}, ".format(number, num), end="")
