#!/usr/bin/python3
""" just return the dict of a class"""


def class_to_json(obj):
    """ Return only the object's dict"""
    return obj.__dict__
