#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_diction = []
    for key, val in a_dictionary.items():
        if val == value:
            my_diction.append(key)
    for key in my_diction:
        a_dictionary.pop(key)
    return a_dictionary
