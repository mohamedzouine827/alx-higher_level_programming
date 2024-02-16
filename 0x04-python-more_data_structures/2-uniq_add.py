#!/usr/bin/python3
def uniq_add(my_list=[]):
    counter = 0
    arr = set(my_list)
    for i in arr:
        counter += i
    return int(counter)
