#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = 0 - number

    num = number % 10
    return num
