#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) not in range(97, 123):
            pass
        else:
            i = chr(ord(i) - ord(' '))
        print("{}".format(i), end="")
    print("")
