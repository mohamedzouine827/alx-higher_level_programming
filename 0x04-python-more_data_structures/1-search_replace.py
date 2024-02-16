#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_copy = my_list.copy()
    for i in range(len(new_copy)):
        if new_copy[i] == search:
            new_copy[i] = replace
    return new_copy
