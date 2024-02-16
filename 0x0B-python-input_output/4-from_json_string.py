#!/usr/bin/python3
"""This module defines a string-to-JSON function"""
import json


def from_json_string(my_str):
    """This module defines a string-to-JSON function"""
    return json.loads(my_str)
