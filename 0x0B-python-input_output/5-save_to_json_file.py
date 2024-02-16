#!/usr/bin/python3
""" write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ Save to json file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
