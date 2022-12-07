#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        score = 0
        name = ""
        for item in a_dictionary:
            if a_dictionary[item] > score:
                score = a_dictionary[item]
                name = item
        return name
    else:
        return None
