#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    mylist = []
    while i < list_length:
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("Division by 0")
            result = 0
        except TypeError:
            print("Wrong Type")
            result = 0
        except IndexError:
            print("Out of range")
            result = 0
        finally:
            mylist.append(result)
            i += 1
    return mylist
