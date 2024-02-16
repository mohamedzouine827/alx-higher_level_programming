#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """Replace the element at a certain position"""
    lenghth = len(my_list)
    if idx > (lenghth - 1) or idx < 0:
        return None
    else:
        return my_list[idx]
