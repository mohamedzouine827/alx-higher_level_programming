#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Print list in reverse order"""
    if isinstance(my_list, list):
        x = my_list[::-1]
        for i in x:
            print("{:d}".format(i))
