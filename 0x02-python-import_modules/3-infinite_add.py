#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    args = sys.argv
    for i in args:
        if i != args[0]:
            total = total + int(i)
    print(total)
