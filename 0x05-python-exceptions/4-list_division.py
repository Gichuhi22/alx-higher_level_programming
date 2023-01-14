#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    newlist = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
            pass
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            pass
        except IndexError:
            print("out of range")
            result = 0
            pass
        finally:
            newlist.append(result)
    return newlist
