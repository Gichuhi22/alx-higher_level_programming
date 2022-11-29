#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
length = len(num)
num_int = int(num[length-1])

if num_int > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,num[length - 1]))
elif num_int == 0:
    print("Last digit of {} is {} and is 0".format(number,num[length - 1]))
elif num_int != 0 and num_int < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,num[length - 1]))
