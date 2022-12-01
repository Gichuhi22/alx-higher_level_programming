#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv
    count = 1
    if len(args) - 1 == 0:
        print("{} arguments.".format(len(args) - 1))
    elif len(args) - 1 == 1:
        print("{} argument:".format(len(args) - 1))
    else:
        print("{} arguments:".format(len(args) - 1))

    for i in args:
        if i != args[0]:
            print("{}: {}".format(count, i))
            count += 1
