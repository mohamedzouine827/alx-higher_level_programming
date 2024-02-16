#!/usr/bin/python3
"""Is it inherits"""


def inherits_from(obj, a_class):
    """ Obj """
    return issubclass(type(obj), a_class) and type(obj) != a_class
