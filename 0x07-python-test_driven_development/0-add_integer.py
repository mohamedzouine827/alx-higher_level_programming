#!/usr/bin/python3
""" Module for add integer """


def add_integer(a, b=98):
    """Add Two integer
    Args:
        a: integer
        b: integer, default 98

    Raises:
        TypeError: if a and b not in float, int

    Return:
        the sum of a and b
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
