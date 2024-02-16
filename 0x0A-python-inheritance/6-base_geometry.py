#!/usr/bin/python3
""" Basic geometry """


class BaseGeometry:
    """ what is the shape?"""
    def area(self):
        raise Exception('area() is not implemented')
