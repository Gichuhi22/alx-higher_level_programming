#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
length = len(num)
num_int = int(num[length-1])


if number < 0 and num_int != 0:
    num_int = 0 - num_int


if num_int > 5:
    print(f"Last digit of {number} is {num_int} and is greater than 5")
elif num_int == 0:
    print("Last digit of {} is {} and is 0".format(number, num_int))
elif num_int != 0 and num_int < 6:
    print(f"Last digit of {number} is {num_int} and is less than 6 and not 0")
