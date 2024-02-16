#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    Max = my_list[0]
    for item in my_list:
        if item > Max:
            Max = item
    return Max
